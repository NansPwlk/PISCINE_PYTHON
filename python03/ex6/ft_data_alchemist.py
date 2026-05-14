import random

NAME_LIST: list[str] = ["Alice", "bob", "Nans", "tom", "Germain",
                        "lea", "Nina", "Patrick", "jeremy"]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {NAME_LIST}")
    new_list_cap: list[str] = [name.capitalize() for name in NAME_LIST]
    print(f"New list with all names capitalized: {new_list_cap}")
    only_cap: list[str] = [name for name in NAME_LIST if name.istitle()]
    print(f"New list of capitalized names only: {only_cap}")
    score_dict: dict = {new_list_cap[i]: random.randint(0, 1000)
                        for i in range(len(new_list_cap))}
    print(f"Score dict: {score_dict}")
    avg_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg_score, 2)}")
    h_score: dict = {name: score for name, score in score_dict.items()
                     if score > avg_score}
    print(f"High scores: {h_score}")


if __name__ == "__main__":
    main()
