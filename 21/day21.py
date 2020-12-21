from pathlib import Path
from aocd import get_data
lines = get_data(day=21, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

# Use pyparsing for fun
import pyparsing as pp
rule = pp.Group(pp.ZeroOrMore(pp.Word(pp.alphas))) + pp.Suppress("(contains ") + \
    pp.Group(pp.ZeroOrMore(pp.Word(pp.alphas) + pp.Optional(pp.Suppress(","))))

# Create a list of all foods and a mapping of allergen to possible foods
allergens = {}
foods = []
for line in lines:
    parts = rule.parseString(line)
    for allerg in parts[1]:
        if allergens.get(allerg) is None:
            allergens[allerg] = set(parts[0])
        allergens[allerg] = allergens[allerg] & set(parts[0])
    foods.extend(list(parts[0]))

# PART A: Now find the all items in `foods` that are not in `allergens`
food_that_has_allergen = [allerg for sublist in allergens.values() for allerg in sublist]
cnt = 0
for food in foods:
    if food not in food_that_has_allergen:
        print(food)
        cnt += 1
print(cnt)

# PART B: Resolve the list of irgendients.
# Find the allergen with only one food, remove it from the list of other foods
# and repeat this process until none is left.
result = {}
prev_len = -1
while prev_len != len(result):
    prev_len = len(result)
    for allerg, foods in allergens.items():
        taken_foods = set(item for item in result.keys())
        this_res = foods - taken_foods
        if len(this_res) == 1:
            result[next(iter(this_res))] = allerg
result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
foods = ",".join([item for item in result.keys()])
print(foods)
pass
