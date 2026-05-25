import ex0


def using_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base_cre = factory.create_base()
    evolved_cre = factory.create_evolved()
    print(f"{base_cre.describe()}")
    print(f"{base_cre.attack()}")
    print(f"{evolved_cre.describe()}")
    print(f"{evolved_cre.attack()}")


def made_combat(fact1: ex0.CreatureFactory, fct2: ex0.CreatureFactory) -> None:
    base_cre = fact1.create_base()
    base_cre2 = fct2.create_base()
    print(f"{base_cre.describe()}")
    print("vs.")
    print(f"{base_cre2.describe()}")
    print("fight!")
    print(f"{base_cre.attack()}")
    print(f"{base_cre2.attack()}")


def main() -> None:
    fire_fact: ex0.FlameFactory = ex0.FlameFactory()
    water_fact: ex0.AquaFactory = ex0.AquaFactory()
    using_factory(fire_fact)
    print()
    using_factory(water_fact)
    print()
    print("Testing battle")
    made_combat(fire_fact, water_fact)


if __name__ == "__main__":
    main()
