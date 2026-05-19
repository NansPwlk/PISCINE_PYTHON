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


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) <= 0:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                proc_name: str = type(proc).__name__
                proc_name = proc_name.replace("Processor", " Processor")
                print(f"{proc_name}: total {len(proc.storage) + proc.rank}"
                      f" items processed, remaining {len(proc.storage)}"
                      " on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)
    batch_1: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)
    print("Send the same batch again")
    stream.process_stream(batch_1)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
