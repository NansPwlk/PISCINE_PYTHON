import math


def get_player_pos() -> tuple:
    is_ok: int = 0
    while is_ok == 0:
        usr_input: str = input("Enter new coordinates as floats in format "
                               "'x,y,z': ")
        split_input: list = usr_input.split(",")
        try:
            my_tuple: tuple[float, float, float] = (float(split_input[0]),
                                                    float(split_input[1]),
                                                    float(split_input[2]))
            is_ok = 1
        except Exception:
            print("Invalid syntax")
            is_ok = 0
    print(f"Got a first tuple: {my_tuple[0:]}")
    return (my_tuple)


def get_second_tuple() -> tuple:
    is_ok: int = 0
    i: int = 0
    while is_ok == 0:
        i = 0
        usr_input: str = input("Enter new coordinates as "
                               "floats in format 'x,y,z': ")
        split_input: list = usr_input.split(",")
        for arg in split_input:
            i += 1
        if i < 3:
            return get_second_tuple()
        try:
            my_tuple: tuple[float, float, float] = (float(split_input[0]),
                                                    float(split_input[1]),
                                                    float(split_input[2]))
            is_ok = 1
        except Exception:
            for j in range(3):
                try:
                    float(split_input[j])
                except Exception:
                    print(f"Error on parameter '{split_input[j]}': "
                          f"could not convert string to float: "
                          f"'{split_input[j]}'")
            is_ok = 0
    return (my_tuple)


def main() -> None:
    my_tuple: tuple = get_player_pos()
    x1, y1, z1 = my_tuple
    print(f"It includes: X:{x1}, Y:{y1}, Z:{z1}")
    distcenter = math.sqrt(x1*x1+y1*y1+z1*z1)
    print(f"Distance to center: {round(distcenter, 4)}\n")
    print("Get a second set of coordinates")
    second_tuple: tuple = get_second_tuple()
    x2, y2, z2 = second_tuple
    distpoint = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distpoint, 4)}")


if __name__ == "__main__":
    main()
