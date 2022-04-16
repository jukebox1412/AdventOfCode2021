from array import *
# https://adventofcode.com/2021/day/6


def main():
    latern_fish_timers = []
    with open("test.txt") as file:
        for line in file:
            split = line.strip().split(',')
            for s in split:
                latern_fish_timers.append(int(s))
    # too slow for 256
    print(calculate_latern_fish_count(latern_fish_timers, 18))

def calculate_latern_fish_count(latern_fish_timers, days):
    i = 0
    while (i < days):
        print(f'day {i}: {len(latern_fish_timers)}')
        current_len_of_timers = len(latern_fish_timers)
        for j in range(0, current_len_of_timers):
            latern_fish_timer = latern_fish_timers[j]
            latern_fish_timer -= 1
            if latern_fish_timer < 0:
                latern_fish_timer = 6
                latern_fish_timers.append(8)
            latern_fish_timers[j] = latern_fish_timer
        i += 1

    return len(latern_fish_timers)

main()
