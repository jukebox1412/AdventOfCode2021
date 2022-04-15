
def main():
    m = 3
    print(find_nb(26825883955641))
import math

def find_nb(m):
    low = math.floor((m ** (1. / 4)) * 1.2) 
    high = math.floor((m ** (1. / 3)) / 9) # get the cubed root of m to find an approximate high
    mid = 0

    # binary search
    while low <= high:
        mid = (high + low) // 2
        answer = doSummation(mid)
        if answer < m:
            low = mid + 1
        elif answer > m:
            high = mid - 1
        else:
            return mid
        
      
 
    return -1

# return the summation
def doSummation(n):
    first_term = n
    second_term = 0
    for i in range(0, n + 1):
        second_term += i * 3

    third_term = 0
    for i in range(0, n + 1):
        third_term += pow(i, 2) * 3
    
    fourth_term = 0
    for i in range(0, n + 1):
        fourth_term += pow(i, 3)

    # {first_term + 1}n^3 - {second_term}n^2 + {third_term}n - {fourth_term} 
    return ((first_term + 1) * pow(n, 3)) - (second_term * pow(n, 2)) + (third_term * n) - fourth_term


main()