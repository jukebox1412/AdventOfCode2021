
def main():
    m = 250500250000
    print(find_nb(m))

saved_numbers = dict()

def find_nb(m):
    current_n = 0
    while(True):
        answer = checkN(current_n, m)
        if answer == m:
            return current_n
        elif answer == -1:
            return -1
        current_n += 1

# return the summation
def checkN(n, m):
    if n in saved_numbers:
        return saved_numbers[n]

    if n == 0: # edge case
        return 1

    i = 0
    total_sum = 0 # total sum starts at 1 because 0^3 is 1

    if len(saved_numbers) > 0:
        i = max(saved_numbers.keys()) # get an early start
        total_sum = saved_numbers[i]

    if total_sum > m: # if n isn't in saved numbers then that means it's not going to be found if total sum is greater
        return -1
    
    while (i < n):
        i += 1
        total_sum += pow(i, 3)
        saved_numbers[i] = total_sum
        if total_sum > m:
            return -1

    saved_numbers[i] = total_sum # one last save
    return total_sum

main()