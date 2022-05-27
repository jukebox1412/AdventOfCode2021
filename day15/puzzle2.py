# https://adventofcode.com/2021/day/15

def main():
    map = list()
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            my_list = list()
            for char in line:
                my_list.append(int(char))
            map.append(my_list)
    map = quintuple_map(map)
    # print_map(map)
    print(dijkstras(map))

def print_map(map: list[list]):
    for i in range(0, len(map)):
        row_str = ""
        for j in range(0, len(map[0])):
            row_str += str(map[i][j])
        print(row_str)

def quintuple_map(map: list[list]) -> list[list]:
    new_map = list()
    for i in range(0, 5):
        for row in map:
            new_row = list()
            for j in range(0, 5):
                for column in row:
                    new_row.append(wrap_10(column + j + i))

            new_map.append(new_row)
        
    return new_map

def wrap_10(num: int) -> int:
    if num < 10:
        return num
    else:
        return num - 9

def dijkstras(map: list[list]):
    opened_list = set()
    closed_list = set()
    cost_to_visit = dict()

    cost_to_visit[(0, 0)] = 0
    opened_list.add((0, 0))

    goal = (len(map) - 1, len(map[0]) - 1)

    while len(opened_list) > 0:
        next_visit = select_lowest_cost(opened_list, cost_to_visit)
        opened_list.remove(next_visit)

        allowed_directions = get_allowed_directions(map, next_visit)
        for allowed_direction in allowed_directions:
            cost_to_visit_allowed_direction = map[allowed_direction[0]
                                                  ][allowed_direction[1]] + cost_to_visit[next_visit]
            if allowed_direction == goal:  # found goal
                return cost_to_visit_allowed_direction


            if allowed_direction not in cost_to_visit:
                cost_to_visit[allowed_direction] = cost_to_visit_allowed_direction

            if cost_to_visit[allowed_direction] < cost_to_visit_allowed_direction:
                continue

            opened_list.add(allowed_direction)

        closed_list.add(next_visit)


def select_lowest_cost(opened_list: set, cost_to_visit: dict):
    lowest_so_far = None
    for location in opened_list:
        if lowest_so_far is None:
            lowest_so_far = location
            continue
        elif cost_to_visit[lowest_so_far] > cost_to_visit[location]:
            lowest_so_far = location
    return lowest_so_far


def get_allowed_directions(map: list[list], current_location: tuple) -> list:
    ret = list()
    left = (current_location[0], current_location[1] - 1)
    right = (current_location[0], current_location[1] + 1)
    up = (current_location[0] - 1, current_location[1])
    down = (current_location[0] + 1, current_location[1])

    if current_location[1] != 0:
        ret.append(left)
    if current_location[1] < len(map[0]) - 1:
        ret.append(right)
    if current_location[0] != 0:
        ret.append(up)
    if current_location[0] < len(map) - 1:
        ret.append(down)

    return ret


main()
