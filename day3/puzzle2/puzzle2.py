def main():
    with open("input.txt") as file:
        all_entries = list()
        
        for line in file:
            line = line.strip()
            all_entries.append(line)

        oxygen_binary = recurse_helper("oxygen", 0, all_entries)[0]
        carbon_binary = recurse_helper("carbon", 0, all_entries)[0]

        oxygen = int(oxygen_binary, 2)
        carbon = int(carbon_binary, 2)
        print(oxygen * carbon)

def recurse_helper(look_for, i, search_list):
    most_common_0 = list()
    most_common_1 = list()

    # returns at most a singular item 
    if len(search_list) == 1:
        return search_list

    for entry in search_list:
        if entry[i] == "0":
            most_common_0.append(entry)
        else:
            most_common_1.append(entry)
    if (look_for == "oxygen"):
        if len(most_common_0) > len(most_common_1):
            return recurse_helper(look_for, i + 1, most_common_0)
        else: # when the number of 1's is equal to or greater than the number of 0's
            return recurse_helper(look_for, i + 1, most_common_1)
    else: # else look for carbon
        if len(most_common_0) <= len(most_common_1):
            return recurse_helper(look_for, i + 1, most_common_0)
        else: # else number of 0's must be greater than the number of 1's
            return recurse_helper(look_for, i + 1, most_common_1)
    

main()