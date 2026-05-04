class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        message = f"The {name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("tomato")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("tomato")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError()
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    main()
