with open("input.txt") as file:
    gamma_binary = ""
    epsilon_binary = ""
    most_common_dict = dict()
    
    
    for line in file:
        line = line.strip()
        for i in range(0, len(line)):
            if i not in most_common_dict:
                most_common_dict[i] = 0
                
            if (line[i] == "0"):
                most_common_dict[i] -= 1
            else:
                most_common_dict[i] += 1
    
    for i in range(0, len(most_common_dict)):
        if most_common_dict[i] < 0: #most common character at i was 0
            gamma_binary += "0"
            epsilon_binary += "1"
        else: # most common character at i was 1
            gamma_binary += "1"
            epsilon_binary += "0"

    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)
    print(gamma * epsilon)