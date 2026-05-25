from ex1.capabilities import HealCapability
from ex0.cre_factory import Creature
from ex0.cre_factory import CreatureFactory


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self, target: str) -> str:
        return (f"Sproutling heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance!")

    def heal(self, target: str) -> str:
        return (f"Bloomelle heals {target} and others for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Sproutling())

    def create_evolved(self) -> Creature:
        return (Bloomelle())
