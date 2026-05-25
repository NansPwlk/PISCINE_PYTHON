import itertools
import typing
import ex0
import ex1


from ex2.strategy import (  # type: ignore
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    BattleStrategy,
    BattleCreature
)


def battle(
    opponents: list[tuple[ex0.CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    participants: list[tuple[BattleCreature, BattleStrategy]] = []
    for factory, strategy in opponents:
        creature = typing.cast(BattleCreature, factory.create_base())
        participants.append((creature, strategy))
    combos = itertools.combinations(participants, 2)
    for (p1_crea, p1_strat), (p2_crea, p2_strat) in combos:
        print("\n* Battle *")
        print(p1_crea.describe())
        print("VS.")
        print(p2_crea.describe())
        print("now fight!")
        try:
            p1_strat.act(p1_crea)
            p2_strat.act(p2_crea)
        except Exception as e:
            print(f"Battle error, aborting tournament: {e}")
            return


def main() -> None:
    flame_fac = ex0.FlameFactory()
    aqua_fac = ex0.AquaFactory()
    heal_fac = ex1.HealingCreatureFactory()
    transform_fac = ex1.TransformCreatureFactory()
    normal_s = NormalStrategy()
    defensive_s = DefensiveStrategy()
    aggressive_s = AggressiveStrategy()
    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([
        (flame_fac, normal_s),
        (heal_fac, defensive_s)
    ])
    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([
        (flame_fac, aggressive_s),
        (heal_fac, defensive_s)
    ])
    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([
        (aqua_fac, normal_s),
        (heal_fac, defensive_s),
        (transform_fac, aggressive_s)
    ])


if __name__ == "__main__":
    main()
