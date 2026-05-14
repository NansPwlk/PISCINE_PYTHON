import sys


def inventory_creation() -> None:
    inv_list: list = []
    arg_list: list = sys.argv[1:]
    i: int = 0
    k: int = 0
    while i < len(arg_list):
        try:
            is_good: list[str] = arg_list[i].split(":")
            for k in range(len(inv_list)):
                if inv_list[k][0] == is_good[0]:
                    raise Exception(f"Redundant item '{inv_list[k][0]}'"
                                    " - discarding")
            if len(is_good) != 2:
                raise Exception(f"Error - invalid parameter '{arg_list[i]}'")
            if not is_good[1].isdigit():
                raise Exception(f"Quantity error for '{is_good[0]}':"
                                " invalid literal for int() with base 10:"
                                f" '{is_good[1]}'")
            inv_list.append(is_good)
        except Exception as error:
            print(f"{error}")
        i += 1
    i = 0
    inventory: dict = {}
    for i in range(len(inv_list)):
        inventory[inv_list[i][0]] = int(inv_list[i][1])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inv_list)} items:"
          f" {sum(list(inventory.values()))}")
    for i in range(len(inv_list)):
        print(f"Item {list(inventory.keys())[i]} represents "
              f"{round((list(inventory.values())[i] /
                        sum(list(inventory.values()))) * 100, 1)}%")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory_creation()


if __name__ == "__main__":
    main()
