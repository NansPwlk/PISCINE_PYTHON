from ex1.capabilities import TransformCapability
from ex0.cre_factory import Creature
from ex0.cre_factory import CreatureFactory


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._state = True
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        self._state = False
        return ("Shiftling returns to normal.")

    def attack(self) -> str:
        msg: str = ""
        if self._state:
            msg = "performs a boosted strike!"
        else:
            msg = "attacks normally."

        return (f"Shiftling {msg}")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._state = True
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        self._state = False
        return ("Morphagon stabilizes its form.")

    def attack(self) -> str:
        msg: str = ""
        if self._state:
            msg = "unleashes a devastating morph strike!"
        else:
            msg = "attacks normally."

        return (f"Morphagon {msg}")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Shiftling())

    def create_evolved(self) -> Creature:
        return (Morphagon())
