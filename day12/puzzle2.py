# https://adventofcode.com/2021/day/12
import copy


class Cave:
    def __init__(self, is_small: bool, name: str):
        self.is_small = is_small
        self.name = name
        self.paths = list()

    def add_path(self, path_to):
        self.paths.append(path_to)

    def __str__(self):
        return f"{self.name}: {[path.__str__() for path in self.paths]}"


def main():
    paths = dict()
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            splits = line.split('-')
            left = splits[0]
            right = splits[1]
            if left not in paths:
                paths[left] = Cave(left.islower(), left)
            if right not in paths:
                paths[right] = Cave(right.islower(), right)

            paths[left].add_path(paths[right])
            paths[right].add_path(paths[left])
    solutions = []
    find_path_to_end(paths['start'], [paths['start']], solutions)
    for solution in solutions:
        print_str = ""
        for cave in solution:
            print_str += cave.name + ','
        # print(print_str)
    print(len(solutions))


def find_path_to_end(cave: Cave, path_history: list, solutions: list):
    if cave.name == 'end':
        solutions.append(path_history)
        return
    for path in cave.paths:  # type: Cave
        new_path_history = list(path_history)
        new_path_history.append(path)
        if not path.is_small: # if big cave
            find_path_to_end(path, new_path_history, solutions) 
        elif (path not in path_history): # if small cave and there's only been 0 visits to this small cave so far
            find_path_to_end(path, new_path_history, solutions) 
        elif not visited_small_cave_twice(path_history) and path.name != 'start': # if there's been no visits to the same small cave twice
            find_path_to_end(path, new_path_history, solutions) 
        



def visited_small_cave_twice(path_history: list) -> bool:
    visited_small_caves = dict()
    for cave in path_history:
        if cave.is_small:
            if cave.name not in visited_small_caves:
                visited_small_caves[cave.name] = 0
            visited_small_caves[cave.name] += 1
            if visited_small_caves[cave.name] > 1:
                return True

    return False


main()
