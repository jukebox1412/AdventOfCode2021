from array import *
# https://adventofcode.com/2021/day/5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.x == __o.x and self.y == __o.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return str([self.x, self.y])

def main():
    with open("input.txt") as file:
        points_hit = dict()
        for line in file:
            split = line.strip().split('->')
            start_point = split[0].strip()
            end_point = split[1].strip()

            points_found = find_points_on_line(start_point, end_point)
            for point in points_found:
                # print(point)
                if point not in points_hit:
                    points_hit[point] = 0
                points_hit[point] += 1
            # print("\n")
            
        total_points_hit_greater_than_1 = 0
        for point in points_hit:
            if points_hit[point] > 1:
                # print(point)
                total_points_hit_greater_than_1 += 1

            

        print(total_points_hit_greater_than_1)


def find_points_on_line(start_point, end_point):
    ret = set()
    start_split = start_point.split(",")
    end_split = end_point.split(",")

    start_x = int(start_split[0].strip())
    start_y = int(start_split[1].strip())

    end_x = int(end_split[0].strip())
    end_y = int(end_split[1].strip())

    ret.add(Point(start_x, start_y))
    ret.add(Point(end_x, end_y))

    if start_x == end_x:
        to_increment = end_y - start_y
        inc_value = sign_func(to_increment)
        # no point starting at 0. That's just the start point that we've already added
        for i in range(1, abs(to_increment)):
            ret.add(Point(start_x, start_y + (i * inc_value)))
    elif start_y == end_y:
        to_increment = end_x - start_x
        inc_value = sign_func(to_increment)
        for i in range(1, abs(to_increment)):
            ret.add(Point(start_x + (i * inc_value), start_y))
    else:
        to_increment = end_x - start_x
        inc_value = sign_func(to_increment)
        # end_x and start_x MUST be non-equal here
        slope = (end_y - start_y) / (end_x - start_x)

        bias = start_y - slope * start_x
        for i in range(1, abs(to_increment)):
            # seems like all slows are just 1 or -1 so we don't need to worry about floats
            new_x = start_x + (i * inc_value)
            new_y = new_x * slope + bias

            if new_y.is_integer():
                ret.add(Point(new_x, int(new_y)))

    return ret


def sign_func(val):
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0


main()
