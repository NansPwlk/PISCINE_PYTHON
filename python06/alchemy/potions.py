import elements
from .elements import create_earth, create_air


def healing_potion() -> str:
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"'{elements.create_fire()}' "  # type: ignore
            f"and '{elements.create_water()}'")  # type: ignore
