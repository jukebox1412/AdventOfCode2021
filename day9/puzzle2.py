# https://adventofcode.com/2021/day/9


from numpy import size


def main():
    map = list()
    with open("input.txt") as file:
        i = 0
        for line in file:
            line = line.strip()
            map.append(list())
            for chr in line:
                map[i].append(int(chr))
            i += 1

    roll_downs = []
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            roll_downs.append(determine_roll_down(i, j, map, set()))

    filtered_roll_downs = filterDistinctResults(roll_downs)
    print(filtered_roll_downs)
    basin_set_sizes = list()
    for roll_down in filtered_roll_downs:
        basin_set = set()
        find_basin(roll_down[1], map, basin_set)
        basin_set_sizes.append(len(basin_set))
    basin_set_sizes.sort()
    basin_set_sizes.reverse()
    print(basin_set_sizes[0] * basin_set_sizes[1] * basin_set_sizes[2])


def find_basin(start_dir, map: list, basin_set: set) -> int:
    basin_set.add(start_dir)
    up = (start_dir[0] - 1, start_dir[1]) if start_dir[0] > 0 else None
    down = (start_dir[0] + 1, start_dir[1]
            ) if start_dir[0] < len(map) - 1 else None
    left = (start_dir[0], start_dir[1] - 1) if start_dir[1] > 0 else None
    right = (start_dir[0], start_dir[1] +
             1) if start_dir[1] < len(map[0]) - 1 else None

    dirs = [up, down, left, right]
    for dir in dirs:
        if dir and map[dir[0]][dir[1]] < 9:
            if dir not in basin_set:
                find_basin(dir, map, basin_set)


def determine_roll_down(i: int, j: int, map: list, history: set):
    # so we don't backtrack
    new_history = set(history)
    new_history.add((i, j))

    up = (i - 1, j) if i > 0 else None
    down = (i + 1, j) if i < len(map) - 1 else None
    left = (i, j - 1) if j > 0 else None
    right = (i, j + 1) if j < len(map[0]) - 1 else None

    dirs = [up, down, left, right]
    current_lowest_dir = None
    current_lowest_value = map[i][j]
    for dir in dirs:
        if dir:
            if map[dir[0]][dir[1]] < current_lowest_value:
                current_lowest_dir = dir
                current_lowest_value = map[dir[0]][dir[1]]
            elif map[dir[0]][dir[1]] == current_lowest_value and dir not in new_history:
                possible_lower_value = determine_roll_down(
                    dir[0], dir[1], map, new_history)[0]
                if possible_lower_value < current_lowest_value:
                    current_lowest_dir = dir
                    current_lowest_value = possible_lower_value

    if current_lowest_dir:
        return determine_roll_down(current_lowest_dir[0], current_lowest_dir[1], map, new_history)
    else:
        return (current_lowest_value, (i, j))


def filterDistinctResults(results):
    filtered = dict()
    for result in results:
        filtered[result[1]] = result[0]

    return [(filtered[key], key) for key in filtered]


main()
