class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def grow(self, howmuch: float) -> None:
        self._height += howmuch

    def age(self, days: int = 1) -> None:
        self._age += days


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 5.0, 90)
    oak = Plant("Oak", 200.0, 365)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()


if __name__ == "__main__":
    main()
