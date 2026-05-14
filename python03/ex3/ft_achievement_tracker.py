import random


ACHIEVEMENTS_LIST: list[str] = ['Crafting Genius', 'Strategist',
                                'World Savior', 'Speed Runner', 'Survivor',
                                'Master Explorer', 'Treasure Hunter',
                                'Unstoppable', 'First Steps',
                                'Collector Supreme',
                                'Untouchable', 'Sharp Mind', 'Boss Slayer']


def gen_player_achievements() -> set[str]:
    nb_achiev: int = random.randint(3, len(ACHIEVEMENTS_LIST))
    achiev_set: set[str] = set(random.sample(ACHIEVEMENTS_LIST, nb_achiev))
    return achiev_set


def main() -> None:
    list_player: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    player: dict = {list_player[0]: gen_player_achievements(),
                    list_player[1]: gen_player_achievements(),
                    list_player[2]: gen_player_achievements(),
                    list_player[3]: gen_player_achievements()}
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {player['Alice']}")
    print(f"Player Bob: {player['Bob']}")
    print(f"Player Charlie: {player['Charlie']}")
    print(f"Player Dylan: {player['Dylan']}")
    print(f"\nAll distinct achievements: {set.union(player['Alice'],
                                                    player['Bob'],
                                                    player['Charlie'],
                                                    player['Dylan'])}")
    print(f"\nCommon achievements: {set.intersection(player['Alice'],
                                                     player['Bob'],
                                                     player['Charlie'],
                                                     player['Dylan'])}")
    print(f"Only Alice: {player['Alice'].difference(player['Bob'],
                                                    player['Charlie'],
                                                    player['Dylan'])}")
    print(f"Only Bob: {player['Bob'].difference(player['Alice'],
                                                player['Charlie'],
                                                player['Dylan'])}")
    print(f"Only Charlie: {player['Charlie'].difference(player['Bob'],
                                                        player['Alice'],
                                                        player['Dylan'])}")
    print(f"Only Dylan: {player['Dylan'].difference(player['Bob'],
                                                    player['Charlie'],
                                                    player['Alice'])}")
    print()
    for i in range(4):
        print(f"{list_player[i]} is missing: "
              f"{set(ACHIEVEMENTS_LIST).difference(player[list_player[i]])}")


if __name__ == "__main__":
    main()
