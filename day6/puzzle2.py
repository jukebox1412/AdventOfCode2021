from array import *
# https://adventofcode.com/2021/day/6


def main():
    latern_fish_timers = []
    with open("input.txt") as file:
        for line in file:
            split = line.strip().split(',')
            for s in split:
                latern_fish_timers.append(int(s))

    print(calculate_latern_fish_count(latern_fish_timers, 256 ))


def get_remaining_fish(to_add_fish, i):
    remaining_fish_count = 0
    for key in to_add_fish:
        if key > i:
            remaining_fish_count += to_add_fish[key]

    return remaining_fish_count


def calculate_latern_fish_count(latern_fish_timers, days):
    fish_on_days = dict()
    to_add_fish = dict()
    total_fish = len(latern_fish_timers)

    for i in range(0, 7):
        fish_on_days[i] = 0
    for i in range(0, len(latern_fish_timers)):
        index = latern_fish_timers[i] % 7
        fish_on_days[index + 1] += 1

    i = 0
    while (i < days + 1):
        if i in to_add_fish:
            fish_on_days[i % 7] += to_add_fish[i]

        total_fish += fish_on_days[i % 7]
        to_add_fish[i + 9] = fish_on_days[i % 7]

        print(f'day {i}: {total_fish} = {total_fish }')
        i += 1

    return total_fish 


main()
