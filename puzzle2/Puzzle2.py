with open("input.txt") as file:
    increases = 0
    prev = -1
    for line in file:
        current = int(line.rstrip())
        if prev == -1:
            prev = current
            continue
        if current > prev:
            increases += 1
        prev = current

    print(increases)