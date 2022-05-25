# https://adventofcode.com/2021/day/15

def main():
    map = [list]
    with open("test.txt") as file:
        for line in file:
            line = line.strip()
            my_list = list()
            for char in line:
                my_list.append(int(char))
            map.append(my_list)


def dijkstras(map: [list]):
    opened_list = list()
    closed_list = list()
    cost_to_visit = dict()
    
    opened_list.append((0,0))
    while len(opened_list) > 0:

        pass


def get_allowed_directions(map: [list], current_location: tuple) -> list:
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
