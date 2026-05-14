import sys


def score_analytics() -> None:
    my_list: list = sys.argv
    new_list: list[int] = []

    print("=== Player Score Analytics ===")
    if len(my_list) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        for i in range(len(my_list[1:])):
            try:
                new_list.append(int(my_list[i+1]))
            except Exception:
                print(f"Invalid parameter: '{my_list[i+1]}'")
        if len(new_list) == 0:
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1> <score2> ...")
        else:
            print(f"Scores processed: {new_list[0:]}")
            print(f"Total players: {len(new_list)}")
            print(f"Total score: {sum(new_list)}")
            print(f"Average score: {sum(new_list) / len(new_list)}")
            print(f"High score: {max(new_list)}")
            print(f"Low score: {min(new_list)}")
            print(f"Score range: {max(new_list) - min(new_list)}\n")


def main() -> None:
    score_analytics()


if __name__ == "__main__":
    main()
