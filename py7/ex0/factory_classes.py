import abc
import typing
import ex0.creature_classes


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> typing.Any:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> typing.Any:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> ex0.creature_classes.Flameling:
        return ex0.creature_classes.Flameling()

    def create_evolved(self) -> ex0.creature_classes.Pyrodon:
        return ex0.creature_classes.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> ex0.creature_classes.Aquabub:
        return ex0.creature_classes.Aquabub()

    def create_evolved(self) -> ex0.creature_classes.Torragon:
        return ex0.creature_classes.Torragon()
