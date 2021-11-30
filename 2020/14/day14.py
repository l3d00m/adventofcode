from pathlib import Path
from aocd import get_data
lines = get_data(day=14, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

# lines = [line.replace("L","#") for line in lines]

import pyparsing as pp
color_name = pp.Combine(pp.Word(pp.alphas) * 2, adjacent=False)
rule = "mem" + "[" + pp.Word(pp.nums) + "]"


mask = 0
reg = {}
for line in lines:
    op, val = line.split(" = ")
    if op == "mask":
        mask = val
    else:
        parsed = rule.parseString(op)
        this_val = int(val)
        this_val = int(mask.replace("X", "1"), 2) & this_val
        this_val = int(mask.replace("X", "0"), 2) | this_val
        reg[parsed[1]] = this_val

print(sum(reg.values()))
pass


# PART 2
from itertools import product
from string import digits
digits = frozenset(digits)


def generate_addresses(base_address):
    options = [(c,) if c != "X" else ("0", "1") for c in base_address]
    return (int(''.join(o), 2) for o in product(*options))


mask = 0
reg = {}
for line in lines:
    op, val = line.split(" = ")
    if op == "mask":
        mask = val
    else:
        base_address = int(''.join(c for c in op if c in digits))
        base_address = list('{:036b}'.format(base_address))
        for i, char in enumerate(mask):
            if char != "0":
                base_address[i] = char
        for address in generate_addresses(base_address):
            reg[address] = int(val)

print(sum(reg.values()))
pass
