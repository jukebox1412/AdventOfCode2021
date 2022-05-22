template = "NCNBCHB"
current = dict()
for i in range(0, len(template) - 1):
    pair = template[i] + template[i + 1]
    if pair not in current:
        current[pair] = 0
    current[pair] += 1

for pair in current:
    print(f"{pair}: {current[pair]}")