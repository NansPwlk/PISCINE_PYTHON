import ex1
import ex0
import typing


class Healer(typing.Protocol):
    def heal(self, target: str) -> str:
        ...


class Transformer(typing.Protocol):
    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


def heal_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base_cre = factory.create_base()
    evolved_cre = factory.create_evolved()
    print("base :")
    print(f"{base_cre.describe()}")
    print(f"{base_cre.attack()}")
    base_heal = typing.cast(Healer, base_cre)
    print(f"{base_heal.heal("itself")}")
    print("evolved :")
    print(f"{evolved_cre.describe()}")
    print(f"{evolved_cre.attack()}")
    evolved_heal = typing.cast(Healer, evolved_cre)
    print(f"{evolved_heal.heal("itself")}")


def transform_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base_cre = factory.create_base()
    evolved_cre = factory.create_evolved()
    print("base :")
    print(f"{base_cre.describe()}")
    print(f"{base_cre.attack()}")
    transformer_base = typing.cast(Transformer, base_cre)
    print(f"{transformer_base.transform()}")
    print(f"{base_cre.attack()}")
    print(f"{transformer_base.revert()}")
    print("evolved :")
    print(f"{evolved_cre.describe()}")
    print(f"{evolved_cre.attack()}")
    transformer_evolved = typing.cast(Transformer, evolved_cre)
    print(f"{transformer_evolved.transform()}")
    print(f"{evolved_cre.attack()}")
    print(f"{transformer_evolved.revert()}")


if __name__ == "__main__":
    heal_fac = ex1.HealingCreatureFactory()
    transform_fac = ex1.TransformCreatureFactory()
    heal_factory(heal_fac)
    print()
    transform_factory(transform_fac)
