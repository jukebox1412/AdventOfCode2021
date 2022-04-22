import statistics
import string

from numpy import number
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

    print(decode_str(lefts, rights))


def turnStringIntoSet(myString: str) -> set:
    ret = set()
    for c in myString:
        ret.add(c)

    return ret


def setToSortedStr(setOfLetters: set) -> str:
    mylist = list(setOfLetters)
    mylist.sort()
    ret = ""
    for s in mylist:
        ret += s
    return ret


def decode_str(lefts: list, rights: list):

    i = 0
    total_sum = 0
    while i < len(lefts):
        left = lefts[i]
        right = rights[i]

        possible_inputs = dict()
        possible_six_inputs = list()
        possible_five_inputs = list()

        # find 1, 4, 7, and 8
        for input in left:
            current_set = turnStringIntoSet(input)
            if len(input) == 2:  # 1
                if 1 not in possible_inputs:
                    possible_inputs[1] = current_set

            elif len(input) == 4:  # 4
                if 4 not in possible_inputs:
                    possible_inputs[4] = current_set

            elif len(input) == 3:  # 7
                if 7 not in possible_inputs:
                    possible_inputs[7] = current_set

            elif len(input) == 7:  # 8
                if 8 not in possible_inputs:
                    possible_inputs[8] = current_set

            elif len(input) == 5:  # 2, 3, 5
                possible_five_inputs.append(current_set)
                pass
            elif len(input) == 6:  # 0, 6, 9
                possible_six_inputs.append(current_set)
                pass

        # find 6
        for possible_six_input in possible_six_inputs:  # type: set
            if not possible_inputs[1].issubset(possible_six_input):  # 6
                possible_inputs[6] = possible_six_input
                # no need to keep it here anymore
                possible_six_inputs.remove(possible_six_input)

        # find 5
        possible_six_inputs_as_list = list(
            possible_six_inputs)  # should contain 0 and 9

        maybe_0 = possible_six_inputs_as_list[0]  # type: set
        maybe_9 = possible_six_inputs_as_list[1]  # type: set

        # finding 0 and 9 too
        maybe_5 = maybe_0.intersection(
            possible_inputs[6])  # maybe_0 is actually 9
        if maybe_5 in possible_five_inputs:
            possible_inputs[5] = maybe_5
            # if maybe_0 is actually 9, then maybe_9 is actually 0
            possible_inputs[0] = maybe_9
            possible_inputs[9] = maybe_0
            possible_five_inputs.remove(maybe_5)

        maybe_5 = maybe_9.intersection(
            possible_inputs[6])  # or maybe_9 is actually 9
        if maybe_5 in possible_five_inputs:
            possible_inputs[5] = maybe_5
            # if maybe_9 is actually 9, then maybe_0 is actually 0
            possible_inputs[0] = maybe_0
            possible_inputs[9] = maybe_9
            possible_five_inputs.remove(maybe_5)

        # find 3
        for maybe_3 in possible_five_inputs:
            if possible_inputs[1].issubset(maybe_3):
                possible_inputs[3] = maybe_3
                possible_five_inputs.remove(maybe_3)

        # last one should be 2
        possible_inputs[2] = list(possible_five_inputs)[0]
        for k in possible_inputs:
            print(f'{k}: {setToSortedStr(possible_inputs[k])}')

        # invert the dictionary so we can lookup by set
        davinci = dict((setToSortedStr(v), k)
                       for k, v in possible_inputs.items())
        number_str: str = ""
        for output in right:
            current_set_str = setToSortedStr(turnStringIntoSet(output))
            number_str += str(davinci[current_set_str])

        total_sum += int(number_str)
        i += 1
    return total_sum


main()
