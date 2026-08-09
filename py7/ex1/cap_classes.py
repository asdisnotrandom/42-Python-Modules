import abc
from ex0.creature_classes import Creature


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(abc.ABC):
    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} attacks normally."
        return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        if self.is_transformed is False:
            self.is_transformed = True
            return f"{self.name} shifts into a sharper form!"
        return f"{self.name} is already transformed!"

    def revert(self) -> str:
        if self.is_transformed is True:
            self.is_transformed = False
            return f"{self.name} returns to normal."
        return f"{self.name} is already reverted!"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed = False

    def attack(self) -> str:
        if self.is_transformed is False:
            return f"{self.name} attacks normally."
        return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self.is_transformed is False:
            self.is_transformed = True
            return f"{self.name} morphs into a dragonic battle form!"
        return f"{self.name} is already transformed!"

    def revert(self) -> str:
        if self.is_transformed is True:
            self.is_transformed = False
            return f"{self.name} stabilizes its form."
        return f"{self.name} is already reverted!"
