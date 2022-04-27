# https://adventofcode.com/2021/day/11
import copy


def main():
    octopus_map = []
    with open("test.txt") as file:
        for line in file:
            current_line = []
            line = line.strip()
            for char in line:
                current_line.append(int(char))
            octopus_map.append(current_line)

    print(count_flashes(octopus_map, 3))


def count_flashes(octopus_map: list, max_steps) -> int:
    ret = 0
    for current_step in range(0, max_steps):
        for row in range(0, len(octopus_map)):
            for col in range(0, len(octopus_map[0])):
                octopus_map[row][col] += 1
        ret += cascade_flashes(octopus_map)
        print(f'step: {current_step + 1}')
        print_map(octopus_map)

    return ret


def print_map(octopus_map: list):
    for row in range(0, len(octopus_map)):
        row_str = ""
        for col in range(0, len(octopus_map[row])):
            row_str += str(octopus_map[row][col]
                           if octopus_map[row][col] < 10 else 0)
        print(row_str)
    print('\n')


def cascade_flashes(octopus_map: list) -> list:
    original_map = None
    flashes = 0

    while original_map != octopus_map:  # keep going as long as the original map is not equal to our newly modified map
        original_map = copy.deepcopy(octopus_map)
        for row in range(0, len(octopus_map)):
            for col in range(0, len(octopus_map[0])):
                if octopus_map[row][col] >= 10:
                    octopus_map[row][col] = -100 # set to negative so we don't double flash
                    up = (row - 1, col) if row > 0 else None
                    down = (row + 1, col) if row < len(octopus_map) - 1 else None
                    left = (row, col - 1) if col > 0 else None
                    right = (row, col + 1) if col < len(octopus_map[0]) - 1 else None

                    up_left = (row - 1, col - 1) if row > 0 and col > 0 else None
                    up_right = (
                        row - 1, col + 1) if row > 0 and col < len(octopus_map[0]) - 1 else None
                    down_left = (row + 1, col - 1) if row < len(octopus_map) - \
                        1 and col > 0 else None
                    down_right = (row + 1, col + 1) if row < len(octopus_map) - \
                        1 and col < len(octopus_map[0]) - 1 else None
                    dirs = [up, down, left, right, up_left,
                            up_right, down_left, down_right]

                    for dir in dirs:
                        if dir:
                            octopus_map[dir[0]][dir[1]] += 1

    # reset flashes to 0 and count flashes
    for row in range(0, len(octopus_map)):
        for col in range(0, len(octopus_map[0])):
            if octopus_map[row][col] < 0:
                octopus_map[row][col] = 0
                flashes += 1

    return flashes


main()
