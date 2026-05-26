from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return (result)
    return (wrapper)


def power_validator(min_power: int) -> Callable:
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            verif: int
            if isinstance(args[0], int):
                verif = args[0]
            else:
                verif = args[2]
            if verif >= min_power:
                return (func(*args, **kwargs))
            else:
                return ("Insufficient power for this spell")
        return (wrapper)
    return (decorator)


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(max_attempts):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if i == max_attempts-1:
                        break
                    print("Spell failed, retrying... "
                          f"(attempt {i+1}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts")
        return (wrapper)
    return (decorator)


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        else:
            return all(char.isalpha() or char == " " for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.099)
        return "Result: Fireball cast!"
    print(fireball())
    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Fizzle")
    try:
        print(unstable_spell())
    except Exception:
        pass

    @retry_spell(3)
    def waagh_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(waagh_spell())
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("Jo"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
