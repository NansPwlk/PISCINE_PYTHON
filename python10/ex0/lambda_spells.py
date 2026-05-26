def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda power: power['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda power: power['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {'max_power': max(mages, key=lambda p: p['power'])['power'],
            'min_power': min(mages, key=lambda p: p['power'])['power'],
            'avg_power': round(sum(map(lambda p: p['power'],
                                       mages)) / len(mages), 2)}


def main() -> None:
    artifacts = [
            {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
            {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
            {'name': 'Wind Cloak', 'power': 65, 'type': 'armor'}
        ]

    mages = [
            {'name': 'Alex', 'power': 75, 'element': 'water'},
            {'name': 'Jordan', 'power': 95, 'element': 'fire'},
            {'name': 'Riley', 'power': 50, 'element': 'earth'}
        ]

    spells = ["fireball", "heal", "shield"]
    print("Testing artifact sorter...")
    print(f"{artifact_sorter(artifacts)}\n")
    print(f"{power_filter(mages, 70)}\n")
    print(f"{spell_transformer(spells)}\n")
    print(f"{mage_stats(mages)}")


if __name__ == "__main__":
    main()
