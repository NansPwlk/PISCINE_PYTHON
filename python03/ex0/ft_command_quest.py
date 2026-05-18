import sys


def command_quest() -> None:
    my_list: list = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {my_list[0]}")
    if len(my_list) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(my_list[1:])}")
        for i in range(len(my_list[1:])):
            print(f"Argument {i+1}: {my_list[i+1]}")
    print(f"Total arguments: {len(my_list)}")


def main() -> None:
    command_quest()


if __name__ == "__main__":
    main()
