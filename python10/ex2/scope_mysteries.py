from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def intern_count() -> int:
        nonlocal count
        count += 1
        return (count)
    return (intern_count)


def spell_accumulator(initial_power: int) -> Callable:
    more_power: int = initial_power

    def accumulation(add_power: int) -> int:
        nonlocal more_power
        more_power += add_power
        return (more_power)
    return (accumulation)


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanter(item: str) -> str:
        return (f"{enchantment_type} {item}")
    return (enchanter)


def memory_vault() -> dict[str, Callable]:
    my_dic: dict = {}

    def store(key: str, value: Any) -> None:
        my_dic[key] = value

    def recall(key: str) -> Any:
        return my_dic.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    test = mage_counter()
    testb = mage_counter()
    print(f"counter_a call 1: {test()}")
    print(f"counter_a call 2: {test()}")
    print(f"counter_b call 1: {testb()}")
    print("\nTesting spell accumulator...")
    accum = spell_accumulator(100)
    print(f"Base 100, add 20: {accum(20)}")
    print(f"Base 100, add 30: {accum(30)}")
    print("\nTesting enchantment factory...")
    flaming_forge = enchantment_factory("Flaming")
    frozen_forge = enchantment_factory("Frozen")
    print(flaming_forge("Sword"))
    print(frozen_forge("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
