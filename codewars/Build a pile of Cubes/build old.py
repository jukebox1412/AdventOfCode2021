
def main():
    m = 1071225
    print(find_nb(m))

saved_numbers = dict()

def find_nb(m):
    n = 0
    total = 0
    while total < m:
        n += 1
        total += pow(n, 3)

    if total > m:
        return -1
    return n


main()