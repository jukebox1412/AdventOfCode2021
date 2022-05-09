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
    find_path_to_end(paths['start'], [paths['start']], solutions=solutions)
    for solution in solutions:
        print_str = ""
        for cave in solution:
            print_str += cave.name + ','
        print(print_str)
    print(len(solutions))
def find_path_to_end(cave: Cave, path_history: list, solutions: list):
    if cave.name == 'end':
        solutions.append(path_history)
        return
    for path in cave.paths: #type: Cave
        if not path.is_small or (path not in path_history):
            new_path_history = list(path_history)
            new_path_history.append(path)
            find_path_to_end(path, new_path_history, solutions)

main()
