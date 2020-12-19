from pathlib import Path
from aocd import get_data
lines = get_data(day=19, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

# Split lines by empty element into parts
from itertools import groupby
parts = [list(g) for k, g in groupby(lines, key=bool) if k]

# Use pyparsing for fun instead of splitting it by hand
import pyparsing as pp
integer = pp.Word(pp.nums).setParseAction(pp.pyparsing_common.convertToInteger)
pp_number_group = pp.Group(pp.OneOrMore(integer) + pp.Optional(pp.Suppress("|")))
pp_literal = pp.Group(pp.Suppress('\"') + pp.Word(pp.alphas) + pp.Suppress('\"'))
pp_rule = integer + pp.Suppress(":") + (pp.OneOrMore(pp_number_group) | pp_literal)
rules = {}
resolved = {}
for line in parts[0]:
    parsed = pp_rule.parseString(line)
    if isinstance(parsed[1][0], str):
        resolved[parsed[0]] = parsed[1]
    else:
        rules[parsed[0]] = parsed[1:]


def resolve(rules, resolved):
    from itertools import product
    ret = []
    for rule in rules:
        strings = []
        for num in rule:
            strings.append(el for el in resolved[num])
        ret.extend(''.join(char) for char in product(*strings))
    return ret


while len(rules) > 1:
    resolved_keys = set(resolved.keys())
    new_rules = rules.copy()
    for key, subrules in rules.items():
        subrule_items = set(item for sublist in subrules for item in sublist)
        if subrule_items.issubset(resolved_keys):
            resolved[key] = resolve(subrules, resolved)
            del new_rules[key]
    rules = new_rules.copy()
    pass
pass


valid_msgs_a = resolve(rules[0], resolved)
matched_msg = set(line for line in parts[1] if line in valid_msgs_a)
print(len(matched_msg))


## PART B

def match_list_forward(lines, items):
    vals = []
    for line in lines:
        for el in items:
            if line.startswith(el):
                vals.append(line[len(el):])
    return vals


# This is basically my own grammer parser. Rules:
# 1. Any of the rule 42 items have to be found at least twice in a row in that string
# 2. After that, the items of rule 32 have to follow at least one time and at max one time less than the items for rule 42
# 3. End condition: The string has to be fully consoumed after iterating like that
for line in (set(parts[1]) - matched_msg):
    match_lines = []
    prev_strings = [line]
    i1 = 0
    while len(prev_strings) > 0:
        prev_strings = match_list_forward(prev_strings, resolved[42])
        match_lines.extend(prev_strings)
        i1 += 1
    i1 -= 1
    if len(match_lines) == 0 or i1 <= 1:
        continue
    prev_strings = match_lines.copy()
    match_lines = []
    i2 = 0
    while len(prev_strings) > 0 and i2 < i1 - 1:
        prev_strings = match_list_forward(prev_strings, resolved[31])
        match_lines.extend(prev_strings)
        i2 += 1
    match_lines = [line for line in match_lines if line == ""]
    if len(match_lines) == 0:
        continue
    matched_msg.add(line)

print(len(matched_msg))
pass
