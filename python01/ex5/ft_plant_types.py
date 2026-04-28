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

    def grow(self, day: int, howmuch: float) -> None:
        for i in range(day):
            self.age()
            self._height += howmuch

    def age(self) -> None:
        self._age += 1

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
        else:
            print("Invalid input...")

    def set_age(self, new_age: int) -> None:
        if isinstance(new_age, int):
            if new_age >= 0:
                self._age = new_age
                print(f"Age updated: {self._age} days old")
            else:
                print(f"{self._name}: Error, age can't be negative")
        else:
            print("Invalid input...")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._bloom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20, 2.1)
    tomato.show()


if __name__ == "__main__":
    main()
