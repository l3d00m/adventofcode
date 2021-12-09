import numpy as np
from aocd import get_data

inp = get_data(day=8, year=2021)
#inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
lines = inp.splitlines()
patterns, outputs = zip(*(s.split(" | ") for s in lines))
patterns = [line.split() for line in patterns]
outputs = [line.split() for line in outputs]

panel_mapping = {0: ["a", "b", "c", "e", "f", "g"],
                 1: ["c", "f"],
                 2: ["a", "c", "d", "e", "g"],
                 3: ["a", "c", "d", "f", "g"],
                 4: ["b", "c", "d", "f"],
                 5: ["a", "b", "d", "f", "g"],
                 6: ["a", "b", "d", "e", "f", "g"],
                 7: ["a", "c", "f"],
                 8: ["a", "b", "c", "d", "e", "f", "g"],
                 9: ["a", "b", "c", "d", "f", "g"],
                 }
print("---Part A---")
sum = 0
for output in outputs:
    for single in output:
        if len(single) in [2, 4, 3, 7]:
            sum += 1

print(sum)
print("---Part B---")

len_mapping = {}
for number, panel in panel_mapping.items():
    if not len_mapping.get(len(panel)):
        len_mapping[len(panel)] = []
    len_mapping[len(panel)].append(number)

is_subset_of = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
for current, this_chars in panel_mapping.items():
    for number, chars in panel_mapping.items():
        if number == current:
            continue
        if set(this_chars).issubset(set(chars)):
            is_subset_of[current].add(number)

sum = 0
for i, pattern in enumerate(patterns):
    signal_mappings = {}
    for signal in pattern:
        possible_numbers = len_mapping[len(signal)]
        if not signal_mappings.get(signal):
            signal_mappings[signal] = set()
        signal_mappings[signal] |= set(possible_numbers)
    mappings = {}
    while (len(mappings) < 9):
        for signal in sorted(signal_mappings, key=lambda k: len(signal_mappings[k])):
            possible_numbers = signal_mappings[signal]
            if (len(possible_numbers)) == 1:
                completed_number = possible_numbers.pop()
                mappings[completed_number] = signal
                signal_chars = set(signal)
                for othersignal, possibles in signal_mappings.items():
                    # remove other items, which are now known to be invalid
                    if not signal_chars.issubset(set(othersignal)):
                        for othernumber in is_subset_of[completed_number]:
                            signal_mappings[othersignal].discard(othernumber)
                    # remove this finished item from all other lists
                    if completed_number in possibles:
                        signal_mappings[othersignal].remove(completed_number)
                del signal_mappings[signal]
        for thisnumber in set(panel_mapping.keys()) - set(mappings.keys()):
            for finishednumber, finishedsignals in mappings.items():
                # remove other items, which are now known to be invalid
                if finishednumber in is_subset_of[thisnumber]:
                    for signal, possible_numbers in signal_mappings.items():
                        if not set(signal).issubset(set(mappings[finishednumber])):
                            signal_mappings[signal].discard(thisnumber)
                    for othernumber in is_subset_of[completed_number]:
                        if othernumber in possibles:
                            signal_mappings[othersignal].remove(othernumber)
    thisvalue = 0
    for i, item in enumerate(reversed(outputs[i])):
        for number, signal in mappings.items():
            if set(item) == set(signal):
                thisvalue += number * 10**i
    sum += thisvalue

print(sum)
print("end")