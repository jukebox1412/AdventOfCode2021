# https://adventofcode.com/2021/day/14

def main():
    template = None
    rules = dict()
    with open("test.txt") as file:
        for line in file:
            line = line.strip()
            if line:
                if not template:
                    template = line
                else:
                    split = line.split(" -> ")
                    rules[split[0]] = split[1]
    for i in range(0, 40):
        template = step(template, rules)

    print(most_common_minus_least_common(template))

def most_common_minus_least_common(template: str) -> int:
    counts = dict()
    for c in template:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    most_common_count = 0
    least_common_count = len(template)
    for c in counts:
        if counts[c] > most_common_count:
            most_common_count = counts[c]
        if counts[c] < least_common_count:
            least_common_count = counts[c]
    return most_common_count - least_common_count


def step(template: str, rules: dict) -> str:
    ret = ""
    for i in range(0, len(template) - 1):
        pair = template[i] + template[i + 1]
        ret += template[i] + rules[pair]

    return ret + template[-1]

main()
