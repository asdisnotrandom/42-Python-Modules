import ex2
import ex0
import ex1
import typing


def tournament(players: list[tuple[ex0.CreatureFactory,
                                   ex2.BattleStrategy]]) -> None:
    print(f"{len(players)} opponents involved")
    try:
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                print("= Battle =")
                print()
                f_creatur: typing.Any = players[i][0].create_base()
                s_creatur: typing.Any = players[j][0].create_base()
                f_strat: typing.Any = players[i][1]
                s_strat: typing.Any = players[j][1]
                print(f_creatur.describe())
                print("= vs =")
                print(s_creatur.describe())
                print("now fight!")
                f_strat.act(f_creatur)
                s_strat.act(s_creatur)

    except ex2.ValidError as e:
        print(f"Battle Error: {e}")


if __name__ == "__main__":
    new_flame: ex0.FlameFactory = ex0.FlameFactory()
    new_aqua: ex0.AquaFactory = ex0.AquaFactory()
    new_healing: ex1.HealingCreatureFactory = ex1.HealingCreatureFactory()
    new_trns: ex1.TransformCreatureFactory = ex1.TransformCreatureFactory()

    new_normal: ex2.NormalStrategy = ex2.NormalStrategy()
    new_aggr: ex2.AggressiveStrategy = ex2.AggressiveStrategy()
    new_def: ex2.DefensiveStrategy = ex2.DefensiveStrategy()

    f_tnt: list[tuple[ex0.CreatureFactory,
                      ex2.BattleStrategy]] = [(new_flame,
                                               new_normal),
                                              (new_healing,
                                               new_def)]
    s_tnt: list[tuple[ex0.CreatureFactory,
                      ex2.BattleStrategy]] = [(new_flame,
                                               new_aggr),
                                              (new_healing,
                                               new_def)]
    t_tnt: list[tuple[ex0.CreatureFactory,
                      ex2.BattleStrategy]] = [(new_aqua,
                                               new_normal),
                                              (new_healing,
                                               new_def),
                                              (new_trns,
                                               new_aggr)]
    print("[(Flameling+Normal), (Healing+Defensive)]")
    print("=== Tournament 0 ===")
    tournament(f_tnt)
    print()
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    print("=== Tournament 1 ===")
    tournament(s_tnt)
    print()
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    print("=== Tournament 2 ===")
    tournament(t_tnt)
