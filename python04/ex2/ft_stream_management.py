import sys
import typing


def ancient_text() -> None:
    arg_list: list = sys.argv
    if len(arg_list) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file: typing.TextIO | None = None
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{arg_list[1]}'")
            file = open(arg_list[1], "r")
            print("---\n")
            content: str = file.read()
            print(f"{content}")
            print("\n---")
        except Exception as error:
            print(f"[STDERR] Error opening file '{arg_list[1]}': {error}",
                  file=sys.stderr)
            return
        finally:
            if file is not None:
                file.close()
                print(f"File '{arg_list[1]}' closed.")
        transform_text(content)


def transform_text(content: str) -> None:
    print("\nTransform data:\n---\n")
    new_file: typing.TextIO | None = None
    try:
        content_list: list[str] = [line + "#" for line in content.split('\n')]
        transform_content: str = '\n'.join(content_list) + "\n"
        print(f"{transform_content}")
        print("\n---\nEnter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file_name: str = sys.stdin.readline()
        new_file_name = new_file_name[:-1]
        if len(new_file_name) == 0:
            print("Not saving data")
            return
        new_file = open(new_file_name, "w")
        new_file.write(transform_content)
        print(f"Data saved in file '{new_file_name}'")
    except Exception as error:
        print(f"[STDERR] Error opening file '{new_file_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return
    finally:
        if new_file is not None:
            new_file.close()


def main() -> None:
    ancient_text()


if __name__ == "__main__":
    main()
