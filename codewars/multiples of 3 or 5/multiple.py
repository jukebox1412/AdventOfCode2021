
def main():
    print(solution(4))


def solution(number):
    summation = 0
    for i in range(1, number):
        doAdd = False

        if i % 3 == 0:
            doAdd = True
        elif i % 5 == 0:
            doAdd = True

        if doAdd:
            summation += i

    return summation


main()
