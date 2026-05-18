import sys
import typing


def ancient_text() -> None:
    arg_list: list = sys.argv
    if len(arg_list) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file: typing.TextIO | None = None
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{arg_list[1]}'")
            file = open(arg_list[1], "r")
            print("---\n")
            print(f"{file.read()}")
            print("\n---")
        except Exception as error:
            print(f"Error opening file '{arg_list[1]}': {error}")
        finally:
            if file is not None:
                file.close()
                print(f"File '{arg_list[1]}' closed.")


def main() -> None:
    ancient_text()


if __name__ == "__main__":
    main()
