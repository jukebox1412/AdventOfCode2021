import statistics

from numpy import diff, number
# https://adventofcode.com/2021/day/7

def main():
    my_input = []
    with open("input.txt") as file:
        for line in file:
            split = line.strip().split(',')
            for s in split:
                my_input.append(int(s))
    print(determine_fuel_cost(my_input))

fibonacci_numbers = dict()

def determine_fuel_cost(my_input : list):
    lowest_total_fuel_cost = 2147483647
    for i in range(min(my_input), max(my_input) + 1):
        total_fuel_cost = 0
        for j in range(0, len(my_input)):
            difference = abs(i - my_input[j])
            fibo_diff = 0
            if difference in fibonacci_numbers:
                fibo_diff = fibonacci_numbers[difference]
            else:
                fibo_diff = find_fibo(difference)
                fibonacci_numbers[difference] = fibo_diff
            total_fuel_cost += fibo_diff
        if total_fuel_cost < lowest_total_fuel_cost:
            lowest_total_fuel_cost = total_fuel_cost
    
    return lowest_total_fuel_cost

def find_fibo(difference: int):
    total_difference = 0
    for i in range(0, difference):
        total_difference += i + 1
    return total_difference

main()
