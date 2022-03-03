from array import *


def main():
    bingo_numbers = list()
    bingo_sheets = list()

    with open("input.txt") as file:
        current_bingo_sheet = {"rows": list(), "columns": list()}
        for line in file:
            line = line.strip()
            line = ' '.join(line.split())
            if len(bingo_numbers) == 0:  # get bingo numbers
                numbers = line.split(",")
                for bingo_number in numbers:
                    bingo_numbers.append(bingo_number)
                continue

            # get puzzles
            if line:
                numbers = line.split(" ")
                current_bingo_row = []
                # in this case, i is the current column index
                for i in range(0, len(numbers)):
                    current_bingo_row.append(numbers[i])

                current_bingo_sheet["rows"].append(current_bingo_row)
                # reset and get a new bingo shset
                if len(current_bingo_sheet["rows"]) > 4:
                    # we have all the rows of the bingo sheet, but lets get all the columns of the bingo sheet too
                    for i in range(0, len(current_bingo_sheet["rows"])):
                        current_bingo_sheet["columns"].append(list())

                    for i in range(0, len(current_bingo_sheet["rows"])):
                        bingo_row = current_bingo_sheet["rows"][i]
                        for j in range(0, len(bingo_row)):
                            current_bingo_sheet["columns"][j].append(
                                bingo_row[j])

                    bingo_sheets.append(current_bingo_sheet)
                    current_bingo_sheet = {"rows": list(), "columns": list()}

    for bingo_number in bingo_numbers:
        for bingo_sheet in bingo_sheets:
            bingo_rows = bingo_sheet["rows"]
            bingo_columns = bingo_sheet["columns"]

            if check_if_win(bingo_rows, bingo_number):
                return


def check_if_win(list_of_lists, bingo_number):
    for alist in list_of_lists:
        print(alist)
        for possible_match in alist:
            if possible_match == bingo_number:
                alist.remove(bingo_number)  # matched number

            if not alist:  # winner!
                # get remaining sum
                print(compute_sum(list_of_lists) * int(bingo_number))
                return True
    return False


def compute_sum(sum_list):
    ret = 0
    print(sum_list)
    for alist in sum_list:
        for item in alist:
            ret += int(item)
            print(f"Current item is {int(item)}, current ret is {ret}")

    return ret


main()
