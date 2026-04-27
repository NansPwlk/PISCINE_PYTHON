def ft_count_harvest_recursive():
    final_day = int(input("Days until harvest: "))
    count_days(final_day, 1)


def count_days(final_day, actual_day):
    print(f"Day {actual_day}")
    if actual_day == final_day:
        print("Harvest time!")
    else:
        return (count_days(final_day, actual_day + 1))
