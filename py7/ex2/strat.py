import abc
from ex1.cap_classes import HealCapability, TransformCapability
from ex0 import CreatureFactory


class ValidError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creatur: CreatureFactory) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creatur: CreatureFactory) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creatur: CreatureFactory) -> bool:
        return True

    def act(self, creatur: CreatureFactory) -> None:
        print(f"{creatur.attack()}")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creatur: CreatureFactory) -> bool:
        if not isinstance(creatur, HealCapability):
            return False
        return True

    def act(self, creatur: CreatureFactory) -> None:
        if not self.is_valid(creatur):
            raise ValidError(f"{creatur.name} needs to be "
                             f"subclass of HealingCapability "
                             f"for Defensive strategy!")
        else:
            print(f"{creatur.attack()}")
            print(f"{creatur.heal()}")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creatur: CreatureFactory) -> bool:
        if not isinstance(creatur, TransformCapability):
            return False
        return True

    def act(self, creatur: CreatureFactory) -> None:
        if not self.is_valid(creatur):
            raise ValidError(f"{creatur.name} needs to be "
                             f"subclass of TransformCapability "
                             f"for Aggressive strategy!")
        else:
            print(f"{creatur.transform()}")
            print(f"{creatur.attack()}")
            print(f"{creatur.revert()}")
