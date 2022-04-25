# https://adventofcode.com/2021/day/10


def main():
    opening_characters = ['(', '[', '{', '<']
    closing_characters = [')', ']', '}', '>']
    point_system = [1, 2, 3, 4]

    my_stacks = dict()
    good_lines = list()
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            my_stack = list()
            bad_line = False
            for char in line:
                if char in opening_characters:
                    my_stack.append(char)
                else:
                    top = my_stack.pop()
                    opening_index = opening_characters.index(top)
                    closing_index = closing_characters.index(char)
                    if opening_index != closing_index:
                        bad_line = True
                        break
            if not bad_line:
                my_stacks[line] = my_stack

    scores = list()
    for line in my_stacks:
        point_total = 0
        current_stack = my_stacks[line]
        current_stack.reverse()
        
        for char in current_stack:
            opening_index = opening_characters.index(char)
            point_total *= 5
            point_total += point_system[opening_index]
        scores.append(point_total)
    scores.sort()

    print(scores[int(len(scores) / 2)])


main()
