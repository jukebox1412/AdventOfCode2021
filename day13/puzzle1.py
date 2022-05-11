# https://adventofcode.com/2021/day/13

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
    with open("input.txt") as file:
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
                if splits[2][0] == 'x':
                    fold_along_x_axis = False
                
                magnitude = int(splits[2].replace('x', '').replace('y', '').replace('=', ''))

                folds.append(Fold(magnitude, fold_along_x_axis))

    for fold in folds:
        fold_points(points, fold)
    
    print(count_points(points))
    print_sheet(points)

def count_points(points: list[Point]):
    distinct_points = set()
    for point in points:
        distinct_points.add((point.x, point.y))
    return len(distinct_points)
    
    
def fold_points(points: list[Point], fold: Fold):
    for point in points:
        point.fold(fold.magnitude, fold.fold_along_x_axis)
    

def print_sheet(points: list[Point]):

    max_x = 0
    max_y = 0
    for point in points:
        print(f"point: {point.x}, {point.y}")
        if point.x > max_x:
            max_x = point.x
        if point.y > max_y:
            max_y = point.y
    
    # print(max_x)
    # print(max_y)
    
    for i in range(0, max_y + 1): # i is the rows (y)
        print_str = ""
        for j in range(0, max_x + 1): # j is the columns (x)
            if any(point.x == j and point.y == i for point in points):
                print_str += "#"
            else:
                print_str += "."
        print(print_str)

main()
