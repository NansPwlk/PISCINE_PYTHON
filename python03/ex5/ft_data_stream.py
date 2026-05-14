import random
import typing

PLAYER_LIST: list[str] = ["Alice", "Bob", "Nans", "Tom", "Germain"]
ACTION_LIST: list[str] = ["move", "grab", "swim", "run", "jump", "use",
                          "climb", "release", "hide", "hit", "eat"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield ((random.choice(PLAYER_LIST), random.choice(ACTION_LIST)))


def consume_event(event_list: list) -> typing.Generator[tuple[str, str],
                                                        None, None]:
    for i in range(len(event_list)):
        event = random.choice(event_list)
        event_list.remove(event)
        yield (event)


def main() -> None:
    my_next: tuple
    my_event: typing.Generator[tuple[str, str], None, None] = gen_event()
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        my_next = next(my_event)
        print(f"Event {i}: Player {my_next[0]} did action {my_next[1]}")
    event_list: list = []
    for i in range(10):
        my_next = next(my_event)
        event_list.append(my_next)
    print(f"Built list of 10 event: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
