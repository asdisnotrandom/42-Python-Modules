from ex0 import CreatureFactory
from .cap_classes import Sproutling, Bloomelle, Shiftling, Morphagon
import typing


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> typing.Any:
        return Sproutling()

    def create_evolved(self) -> typing.Any:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> typing.Any:
        return Shiftling()

    def create_evolved(self) -> typing.Any:
        return Morphagon()
