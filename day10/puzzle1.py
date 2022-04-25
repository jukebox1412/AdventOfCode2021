# https://adventofcode.com/2021/day/10


def main():
    point_total = 0
    opening_characters = ['(', '[', '{', '<']
    closing_characters = [')', ']', '}', '>']
    point_system = [3, 57, 1197, 25137]
    with open("input.txt") as file:
        for line in file:
            my_stack = list()
            line = line.strip()
            for char in line:
                if char in opening_characters:
                    my_stack.append(char)
                else: 
                    top = my_stack.pop()
                    opening_index = opening_characters.index(top)
                    closing_index = closing_characters.index(char)
                    if opening_index != closing_index:
                        point_total += point_system[closing_index]
                        break
    print(point_total)
                    


main()
