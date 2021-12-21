import numpy as np
from aocd import get_data
from collections import Counter

inp = get_data(day=14, year=2021)

template, insertions = inp.split("\n\n")
insertions = [tuple(line.split(" -> ")) for line in insertions.splitlines()]
insertions = dict(insertions)

pairs_counter = Counter()
for i in range(len(template) - 1):
    pairs_counter[template[i] + template[i + 1]] += 1

result_counter = Counter(template)
for i in range(40):
    next_pairs_counter = Counter()
    for pair, pair_count in pairs_counter.items():
        new_letter = insertions[pair]
        next_pairs_counter[pair[0] + new_letter] += pair_count
        next_pairs_counter[new_letter + pair[1]] += pair_count
        result_counter[new_letter] += pair_count
    pairs_counter = next_pairs_counter
    if i == 9:  # part A
        print(result_counter.most_common()[0][1] - result_counter.most_common()[-1][1])

print(result_counter.most_common()[0][1] - result_counter.most_common()[-1][1])
print("end")
