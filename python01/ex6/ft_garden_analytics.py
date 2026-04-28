class Plant:
    class _Statistic:
        def __init__(self) -> None:
            self._show: int = 0
            self._age: int = 0
            self._grow: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, ", end="")
            print(f"{self._show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._statistic = self._Statistic()
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
        self._statistic._show += 1
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self, howmuch: float) -> None:
        self._statistic._grow += 1
        self._height += howmuch

    def age(self, days: int = 1) -> None:
        self._statistic._age += 1
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

    @staticmethod
    def is_year(how_many: int) -> bool:
        if how_many > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


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
    class _Tree_stat(Plant._Statistic):
        def __init__(self) -> None:
            super().__init__()
            self._shade: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._statistic: Tree._Tree_stat = self._Tree_stat()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._statistic._shade += 1


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

    def grow(self, howmuch: float) -> None:
        super().grow(howmuch)
        self._nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._nb_seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._nb_seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._nb_seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._statistic.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()
    print("=== Anonymous")
    mystery = Plant.anonymous()
    mystery.show()
    display_stats(mystery)


if __name__ == "__main__":
    main()
