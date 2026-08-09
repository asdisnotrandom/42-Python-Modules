import abc
from ex0.creature_classes import Creature
from ex1.cap_classes import HealCapability, TransformCapability


class ValidError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(abc.ABC):
    def __init__(self, creatur: Creature) -> None:
        if not isinstance(self.creatur, Creature):
            raise ValidError(f"{self.creatur} is not a Creature!")
            return False
        else:
            self.creatur = creatur

    @abc.abstractmethod
    def is_valid(self) -> bool:
        pass

    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creatur: Creature) -> None:
        super().__init__(creatur)

    def is_valid(self) -> bool:
        return True

    def act(self) -> None:
        pass


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creatur: Creature) -> None:
        super().__init__(creatur)

    def is_valid(self) -> bool:
        if not isinstance(self.creatur, HealCapability):
            raise ValidError(f"Battle Error: {self.creatur} needs to be"
                                 f"subclass of HealingCapability"
                                 f"for Defensive strategy!")
            return False
        return True

    def act(self) -> None:
        pass


class AggressiveStrategy(BattleStrategy):
    def __init__(self, creatur: Creature) -> None:
        super().__init__(creatur)

    def is_valid(self) -> bool:
        if not isinstance(self.creatur, TransformCapability):
            raise ValidError(f"Battle Error: {self.creatur} needs to be"
                                f"subclass of TransformCapability"
                                f"for Aggressive strategy!")
            return False
        return True

    def act(self) -> None:
        pass 