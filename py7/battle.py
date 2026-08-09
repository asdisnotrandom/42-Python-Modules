import ex0
import typing


def show_functionality(factory_given: ex0.CreatureFactory) -> None:
    new_base: typing.Any = factory_given.create_base()
    print(f"{new_base.describe()}")
    print(f"{new_base.attack()}")
    new_evolved: typing.Any = factory_given.create_evolved()
    print(f"{new_evolved.describe()}")
    print(f"{new_evolved.attack()}")


def base_fight(factory_one: ex0.CreatureFactory,
               factory_two: ex0.CreatureFactory) -> None:
    first_creature: typing.Any = factory_one.create_base()
    second_creature: typing.Any = factory_two.create_base()
    print(f"{first_creature.describe()}")
    print("==== vs ====")
    print(f"{second_creature.describe()}")
    print("==== fight ====")
    print(f"{first_creature.attack()}")
    print(f"{second_creature.attack()}")


if __name__ == "__main__":
    new_flame: ex0.CreatureFactory = ex0.FlameFactory()
    new_aqua: ex0.CreatureFactory = ex0.AquaFactory()
    show_functionality(new_flame)
    print()
    show_functionality(new_aqua)
    print()
    base_fight(new_flame, new_aqua)
