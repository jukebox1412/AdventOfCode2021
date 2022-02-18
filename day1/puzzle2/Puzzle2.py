with open("input.txt") as file:
    increases = 0
    file_list = list()
    for line in file:
        current = int(line.rstrip())
        file_list.append(current)
    
    i = 0
    previous_three_window_total = 0 
    current_three_window_total = 0
    
    while i < len(file_list) - 2:
        current_three_window_total = file_list[i] + file_list[i + 1] + file_list[i + 2]
        
        if previous_three_window_total != 0:
            if previous_three_window_total < current_three_window_total:
                increases += 1

        previous_three_window_total = current_three_window_total
        i += 1
    print(increases)