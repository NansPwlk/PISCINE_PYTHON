import abc


class Creature(abc.ABC):
    def __init__(self, name: str, cre_type: str) -> None:
        self._name: str = name
        self._cre_type: str = cre_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self._name} is a {self._cre_type} type Creature")


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass
