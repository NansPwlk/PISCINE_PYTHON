import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    action: Callable
    if len(spells) == 0:
        return (0)
    elif operation == "add":
        action = operator.add
    elif operation == "multiply":
        action = operator.mul
    elif operation == "max":
        action = max
    elif operation == "min":
        action = min
    else:
        raise ValueError("Unknown operation")
    return functools.reduce(action, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fclone: Callable = functools.partial(base_enchantment, power=50,
                                         element="Fire")
    iclone: Callable = functools.partial(base_enchantment, power=50,
                                         element="Ice")
    wclone: Callable = functools.partial(base_enchantment, power=50,
                                         element="Water")
    my_dict: dict = {
        "Fire": fclone,
        "Ice": iclone,
        "Water": wclone
    }
    return (my_dict)


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return (0)
    elif n == 1:
        return (1)
    else:
        return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return (f"Damage spell: {arg} damage")
        pass

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return (f"Enchantment: {arg}")
        pass

    @dispatcher.register(list)
    def _(arg: list) -> str:
        return (f"Multi-cast: {len(arg)} spells")
        pass
    return dispatcher


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [40, 30, 20, 10]
    print(f"Sum: {spell_reducer(spells.copy(), 'add')}")
    print(f"Product: {spell_reducer(spells.copy(), 'multiply')}")
    print(f"Max: {spell_reducer(spells.copy(), 'max')}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["spell1", "spell2", "spell3"]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
