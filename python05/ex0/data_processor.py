import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        content_return: str = self.storage.pop(0)
        rank_return: int = self.rank
        self.rank += 1
        return (rank_return, content_return)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int):
            return True
        elif isinstance(data, float):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception
        else:
            if isinstance(data, list):
                for item in data:
                    self.storage.append(str(item))
            else:
                self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception
        else:
            if isinstance(data, list):
                for item in data:
                    self.storage.append(item)
            else:
                self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) and isinstance(value, str) for key,
                       value in data.items())
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                elif not all(isinstance(key, str)
                             and isinstance(value, str) for key,
                             value in item.items()):
                    return False
            return True
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception
        else:
            text_return: str = ""
            if isinstance(data, list):
                for item in data:
                    text_return = f"{item['log_level']}: {item['log_message']}"
                    self.storage.append(text_return)
            else:
                text_return = f"{data['log_level']}: {data['log_message']}"
                self.storage.append(text_return)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest('foo')
    except Exception:
        print("Got exception: Improper numeric data")
    data_num: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    num_proc.ingest(data_num)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    data_text: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {data_text}")
    text_proc.ingest(data_text)
    print("Extracting 1 value...")
    rank_text, val_text = text_proc.output()
    print(f"Text value {rank_text}: {val_text}")
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    data_log: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {data_log}")
    log_proc.ingest(data_log)
    print("Extracting 2 values...")
    for _ in range(2):
        rank_log, val_log = log_proc.output()
        print(f"Log entry {rank_log}: {val_log}")


if __name__ == "__main__":
    main()
