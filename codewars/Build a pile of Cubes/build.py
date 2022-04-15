
def main():
    print(find_nb(91716553919377))


def find_nb(m):
    total = 0
    n = 0
    while (total < m):
        n += 1
        total += pow(n, 3)

    if total == m:
        return n
    return -1

main()