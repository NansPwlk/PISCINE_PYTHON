import abc
import typing


class BattleCreature(typing.Protocol):
    def describe(self) -> str:
        ...

    def attack(self) -> str:
        ...


class HealerProtocol(typing.Protocol):
    def heal(self, target: str) -> str:
        ...


class TransformerProtocol(typing.Protocol):
    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: BattleCreature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: BattleCreature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: BattleCreature) -> bool:
        return True

    def act(self, creature: BattleCreature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.__class__.__name__}"
                             "' for this aggressive strategy")
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: BattleCreature) -> bool:
        return (hasattr(creature, "heal"))

    def act(self, creature: BattleCreature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.__class__.__name__}"
                             "' for this aggressive strategy")
        print(creature.attack())
        healer_creature = typing.cast(HealerProtocol, creature)
        print(healer_creature.heal("itself"))


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: BattleCreature) -> bool:
        return (hasattr(creature, "transform"))

    def act(self, creature: BattleCreature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.__class__.__name__}"
                             "' for this aggressive strategy")
        transform_creature = typing.cast(TransformerProtocol, creature)
        print(transform_creature.transform())
        print(creature.attack())
        print(transform_creature.revert())
