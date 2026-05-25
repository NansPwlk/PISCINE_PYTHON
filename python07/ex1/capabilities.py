import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(abc.ABC):
    def __init__(self, state: bool = False) -> None:
        self._state = state

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass
