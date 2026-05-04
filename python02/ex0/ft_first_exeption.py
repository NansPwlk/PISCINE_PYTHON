def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
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


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
