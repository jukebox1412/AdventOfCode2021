import statistics
# https://adventofcode.com/2021/day/7

def main():
    lefts = []
    rights = []

    with open("input.txt") as file:
        for line in file:
            split = line.strip().split(' | ')
            left = split[0].split(' ') 
            right = split[1].split(' ') 
            lefts.append(left)
            rights.append(right)
    print(calc_1478(lefts, rights))

def calc_1478(lefts, rights):
    count = 0
    for right in rights:
        for output in right:
            if len(output) == 2: # 1
                count += 1
            elif len(output) == 4: # 4
                count += 1
            elif len(output) == 3: # 7
                count += 1
            elif len(output) == 7: # 8
                count += 1

    return count
main()
