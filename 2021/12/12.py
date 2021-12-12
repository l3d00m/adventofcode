import numpy as np
from aocd import get_data
from collections import Counter

inp = get_data(day=12, year=2021)
lines = inp.splitlines()
#numbers = [int(line) for line in lines]
#arrayinp = np.asarray(numbers)

paths = [line.split("-") for line in lines]

#print(numbers)

print("---Part A---")


def find_next(current_el, current_chain, partb=False):
    possible_next = []
    for path in paths:
        if current_el in path:
            if current_el == path[0]:
                new_el = path[1]
            elif current_el == path[1]:
                new_el = path[0]
            if new_el == "start":
                continue
            if new_el.islower():
                if partb:
                    lowers = [itm for itm in current_chain if itm.islower()]
                    if (not Counter(lowers).most_common()[0][1] >= 2 and new_el in lowers:
                        continue
                else:
                    if new_el in current_chain:
                        continue
            possible_next.append(new_el)
    return possible_next


def iterate(partb=False):
    chains=[["start"]]
    finished_chains=[]
    while True:
        for i, chain in enumerate(chains):
            next_els=find_next(chain[-1], chain, partb=partb)
            for next_el in next_els:
                new_chain=chain.copy()
                new_chain.append(next_el)
                if new_chain[-1] != "end":
                    chains.append(new_chain)
                else:
                    finished_chains.append(new_chain)
            chains.remove(chain)
            break
        if len(chains) == 0:
            break
    print(len(finished_chains))


iterate()

print("---Part B---")
iterate(partb=True)


print("end")
