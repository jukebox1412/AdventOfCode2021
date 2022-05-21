# https://adventofcode.com/2021/day/14


from math import floor


MAX_CACHE_LENGTH = 16
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
                    rules[split[0]] = split[0][0] + split[1] + split[0][1]
    cache = rules
    
    for i in range(0, 2):
        template = step(template, cache)

    print(template)
    for cached in cache:
        print(f"[{cached}]:[{cache[cached]}]")

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


def step(template: str, cache: dict) -> str:
    i = 0
    original_template = template
    while i < len(template) - 1:
        for j in reversed(range(i + 1, min(len(template), i + MAX_CACHE_LENGTH))):
            if template[i:j+1] in cache:
                jump_ahead = len(cache[template[i:j+1]])
                template = template[:i] + cache[template[i:j+1]] + template[j+1:]
                i += jump_ahead - 2
                break # break because reversed and we need to jump ahead
        i += 1

    # update the cache
    for i in range(0, len(original_template) - 3): # minus 3 because we already have the len 2 combinations cached
        for j in range(i + 3, min(i + MAX_CACHE_LENGTH, len(original_template))):
            new_i = i + int((i + 1) / 2) 
            new_j = j + int((j + 1) / 2)
            cache[original_template[i:j]] = template[new_i:new_j + 1]

            

    return template
            


main()
