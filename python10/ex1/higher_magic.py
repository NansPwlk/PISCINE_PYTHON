from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball scorches {target} dealing {power} fire damage"


def transmute(target: str, power: int) -> str:
    return f"Alchemic transmut turn {target} into element using {power} energy"


def reaper_slash(target: str, power: int) -> str:
    return f"God of Death strikes {target} with a {power} power RNG slash"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combinator(target: str, power: int) -> tuple:
        result: str = spell1(target, power)
        result_bis: str = spell2(target, power)
        return (result, result_bis)
    return combinator


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplificator(target: str, power: int) -> str:
        power = power * multiplier
        return (base_spell(target, power))
    return amplificator


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def castor(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return castor


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequencor(target: str, power: int) -> list:
        return (list(map(lambda s: s(target, power), spells)))
    return sequencor


def main() -> None:
    target = "Nans"
    power = 42
    print("--- 1. Testing Combiner ---")
    combo = spell_combiner(heal, reaper_slash)
    print(f"Combined: {combo(target, power)}")
    print("\n--- 2. Testing Amplifier ---")
    amped = power_amplifier(fireball, 5)
    print(f"Amplified (x5): {amped(target, power)}")
    print("\n--- 3. Testing Conditional Caster ---")

    def is_powerful(t: str, p: int) -> bool:
        return p > 30
    caster = conditional_caster(is_powerful, transmute)
    print(f"Test (Power 42): {caster(target, 42)}")
    print(f"Test (Power 10): {caster(target, 10)}")
    print("\n--- 4. Testing Sequence Caster ---")
    seq = spell_sequence([heal, fireball, transmute, reaper_slash])
    results = seq(target, power)
    for res in results:
        print(f"Sequenced: {res}")


if __name__ == "__main__":
    main()
