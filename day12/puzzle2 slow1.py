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
    find_path_to_end(paths['start'], ['start'], solutions=solutions)
    total = 0
    for solution in solutions:
        small_cave_visits = dict()
        twice_small_cave_visits = 0
        for cave in solution: # type: str
            if cave.islower():
                if cave not in small_cave_visits:
                    small_cave_visits[cave] = 0
                small_cave_visits[cave] += 1
                if small_cave_visits[cave] > 1:
                    twice_small_cave_visits += 1    
                if twice_small_cave_visits > 1:
                    break # outer break
        else: 
            total += 1
            print_str = ""

            for cave in solution: # type: str
                if cave.islower():
                    if cave not in small_cave_visits:
                        small_cave_visits[cave] = 0
                    small_cave_visits[cave] += 1
                print_str += cave + ','
            
            print_str = print_str[0:len(print_str)-1] # remove the last comma
            print(print_str)

    print(total)


def find_path_to_end(cave: Cave, path_history: list, solutions: list):
    if cave.name == 'end':
        solutions.append(path_history)
        return
    for path in cave.paths:  # type: Cave
        number_of_times_visited = path_history.count(path.name)
        if not path.is_small or (path.name != 'start' and number_of_times_visited < 2):
            new_path_history = list(path_history)
            new_path_history.append(path.name)
            find_path_to_end(path, new_path_history, solutions)


main()
