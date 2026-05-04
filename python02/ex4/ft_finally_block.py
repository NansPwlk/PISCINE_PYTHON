class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        message = f"Invalid plant name to water: '{name}'"
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"{plant_name}")


def test_watering_systems() -> None:
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    print("Closing watering systems\n")
    print("Testing invalid plants...")
    test_watering_systems()


if __name__ == "__main__":
    main()
