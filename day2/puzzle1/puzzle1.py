with open("test.txt") as file:
    forward_total = 0
    depth_total = 0
    
    for line in file:
        splits = line.strip().split()
        direction = splits[0]
        magnitude = int(splits[1])
        if direction == "forward":
            forward_total += magnitude
        elif direction == "up":
            depth_total -= magnitude
        else:
            depth_total += magnitude # else it's down


    print(forward_total * depth_total)