def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError(f"{temp_int}°C is too colds for plants (min 0°C)")
    return (temp_int)


def test_temperature() -> None:
    print("Input date is '25'")
    try:
        temp = input_temperature('25')
        print(f"Temperature is now {temp}°C\n")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    print("Input date is 'abc'")
    try:
        temp = input_temperature('abc')
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")
    print("Input date is '100'")
    try:
        temp = input_temperature('100')
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")
    print("Input date is '-50'")
    try:
        temp = input_temperature('-50')
        print(f"Temperature is now {temp}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
