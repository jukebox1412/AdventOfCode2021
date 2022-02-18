with open("input.txt") as file:
    forward_total = 0
    current_aim = 0
    depth_total = 0
    
    for line in file:
        splits = line.strip().split()
        direction = splits[0]
        magnitude = int(splits[1])
        if direction == "forward":
            forward_total += magnitude
            depth_total += current_aim * magnitude
        elif direction == "up":
            current_aim -= magnitude
        else:
            current_aim += magnitude # else it's down


    print(forward_total * depth_total)