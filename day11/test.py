import copy
list_1 = list([list([1]), list([2])])
list_2 = copy.deepcopy(list_1)
list_1[0][0] += 0
if list_1 == list_2:
    print("foobar")