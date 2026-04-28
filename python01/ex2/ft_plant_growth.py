class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm"
              f", {self._age} days old")

    def grow(self, howmuch: float) -> None:
        self._height += howmuch

    def age(self, days: int = 1) -> None:
        self._age += days


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    howmuch = 0.8
    days_to_grow = 7
    for i in range(days_to_grow):
        print(f"=== Day {i+1} ===")
        rose.age()
        rose.grow(howmuch)
        rose.show()
    total_growth = howmuch * days_to_grow
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
