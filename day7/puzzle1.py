import statistics
# https://adventofcode.com/2021/day/7

def main():
    my_input = []
    with open("input.txt") as file:
        for line in file:
            split = line.strip().split(',')
            for s in split:
                my_input.append(int(s))
    print(determine_fuel_cost(my_input))

def determine_fuel_cost(my_input : list):
    median = statistics.median(my_input)
    print(f'median is {median}')
    total_fuel_cost = 0
    for i in range(0, len(my_input)):
        total_fuel_cost += abs(median - my_input[i])
    return int(total_fuel_cost)
main()
