# https://adventofcode.com/2021/day/13

from cv2 import magnitude


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def fold(self, magnitude: int, fold_along_x_axis: bool):
        if not fold_along_x_axis:
            if self.x < magnitude:
                return  # no need for any further computation
            distance_to_magnitude = self.x - magnitude
            self.x -= distance_to_magnitude * 2
        else:
            if self.y < magnitude:
                return  # no need for any further computation
            distance_to_magnitude = self.y - magnitude
            self.y -= distance_to_magnitude * 2


class Fold:
    def __init__(self, magnitude: int, fold_along_x_axis: bool) -> None:
        self.magnitude = magnitude
        self.fold_along_x_axis = fold_along_x_axis


def main():
    points = list[Point]()
    folds = list[Fold]()
    single_break = False
    with open("test.txt") as file:
        for line in file:
            line = line.strip()
            if not line:
                single_break = True
                continue

            if not single_break:  # look for points
                splits = line.split(',')
                
                x = int(splits[0])
                y = int(splits[1])

                points.append(Point(x, y))
            else:  # look for folds
                splits = line.split(' ')
                
                fold_along_x_axis = True
                if splits[3][0] == 'x':
                    fold_along_x_axis = False
                
                magnitude = int(splits[3][2])

                folds.append(Fold(magnitude, fold_along_x_axis))

    print(points)
    print(folds)

def print_sheet(points: list[Point]):
    max_x = 0
    max_y = 0
    for point in points:
        if point.x > max_x:
            max_x = point.x
        if point.y > max_y:
            max_y = point.y
    
    for i in range(0, max_x):
        print_str = ""
        for j in range(0, max_y):
            if any(point.x == i and point.y == j for point in points):
                print_str += "#"
            else:
                print_str += "."
        print(print_str)

main()
