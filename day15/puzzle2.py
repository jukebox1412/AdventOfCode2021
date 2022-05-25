# https://adventofcode.com/2021/day/14

def main():
    template = None
    rules = dict()
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                if not template:
                    template = line
                else:
                    split = line.split(" -> ")
                    rules[split[0]] = split[1]

    current = dict()
    for i in range(0, len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair not in current:
            current[pair] = 0
        current[pair] += 1

    for i in range(0, 40):
        next_current = dict()       
        for pair in current:
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            
            if new_pair_1 not in next_current:
                next_current[new_pair_1] = 0
            if new_pair_2 not in next_current:
                next_current[new_pair_2] = 0

            next_current[new_pair_1] += current[pair]
            next_current[new_pair_2] += current[pair]

        current = next_current

    # for pair in current:
    #     print(f"{pair}: {current[pair]}")
    print(most_common_minus_least_common(next_current, template[-1]))


def most_common_minus_least_common(current: dict, last_letter: str) -> int:
    counts = dict()
    max_possible = 1
    counts[last_letter] = 1
    for pair in current:
        c1 = pair[0]
        if c1 not in counts:
            counts[c1] = 0
        counts[c1] += current[pair]
        max_possible += current[pair]

    most_common_count = 0
    least_common_count = max_possible
    for c in counts:
        if counts[c] > most_common_count:
            most_common_count = counts[c]
        if counts[c] < least_common_count:
            least_common_count = counts[c]
    return most_common_count - least_common_count




main()
