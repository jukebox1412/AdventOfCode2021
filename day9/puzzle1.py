# https://adventofcode.com/2021/day/9


def main():
    map = list()
    with open("test.txt") as file:
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
            roll_downs.append(determine_roll_down(i, j, map))
    print(filterDistinctResults(roll_downs))


def determine_roll_down(i: int, j: int, map: list):
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

    if current_lowest_dir:
        return determine_roll_down(current_lowest_dir[0], current_lowest_dir[1], map)
    else:
        return (current_lowest_value, (i, j))

def filterDistinctResults(results):
    ret = dict()
    for result in results:
        ret[result[1]] = result[0]
    return ret

main()
