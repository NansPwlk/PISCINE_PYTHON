class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if isinstance(height, float) and isinstance(age, int):
            if height < 0 or age < 0:
                print("Not this time, negative number")
            else:
                self._name = name
                self._height = height
                self._age = age
        else:
            print("Not this time, invalid type")

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self, howmuch: float) -> None:
        self._height += howmuch

    def age(self, days: int = 1) -> None:
        self._age += days

    def get_height(self) -> None:
        print(f"Height is {self._height}.")

    def get_age(self) -> None:
        print(f"Age is {self._age} day.")

    def set_height(self, new_height: float) -> None:
        if isinstance(new_height, float):
            if new_height >= 0:
                self._height = new_height
                print(f"Height updated: {round(self._height)}cm")
            else:
                print(f"{self._name}: Error, height can't be negative")
                print("Height update rejected")
        else:
            print("Invalid input...")

    def set_age(self, new_age: int) -> None:
        if isinstance(new_age, int):
            if new_age >= 0:
                self._age = new_age
                print(f"Age updated: {self._age} days old")
            else:
                print(f"{self._name}: Error, age can't be negative")
                print("Age update rejected")
        else:
            print("Invalid input...")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-42.0)
    rose.set_age(-42)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
