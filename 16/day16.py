from aocd import get_data
lines = get_data(day=16, year=2020).splitlines()

# Split lines by empty element into parts
from itertools import groupby
parts = [list(g) for k, g in groupby(lines, key=bool) if k]

# Create rule for parsing "departure location: 37-479 or 485-954" into name and ranges
import pyparsing as pp
range_rule = pp.Group(pp.Word(pp.nums) + pp.Suppress("-") + pp.Word(pp.nums))
field_rule = ... + pp.Suppress(":") + pp.Group(pp.OneOrMore(range_rule + pp.Optional(pp.Suppress("or"))))
valid_rows = {}
valid_numbers = set()
for line in parts[0]:
    parsed = field_rule.parseString(line)
    this_numbers = []
    for r in parsed[1]:
        this_numbers.extend(list(range(int(r[0]), int(r[1]) + 1)))
    valid_rows[parsed[0]] = this_numbers
    valid_numbers |= set(this_numbers)

your_ticket = [int(entry) for entry in parts[1][1].split(",")]
ticket_len = len(your_ticket)
nearby_tickets = []
for line in parts[2]:
    if line.startswith("nearby"):
        continue
    nearby_tickets.append([int(entry) for entry in line.split(",")])

### Part A
error_rate = 0
for ticket in nearby_tickets:
    for val in ticket:
        if val not in valid_numbers:
            error_rate += val

print(error_rate)


### Part B
def is_valid(ticket, valid_items):
    for val in ticket:
        if val not in valid_items:
            return False
    return True


# Filter out any invalid tickets and create row matrix
valid_tickets = []
rows = [[] for i in range(ticket_len)]
for ticket in nearby_tickets:
    if is_valid(ticket, valid_numbers):
        valid_tickets.append(ticket)
        for i, num in enumerate(ticket):
            rows[i].append(num)

# Store all possible rows for every field
possible = {}
for i, row in enumerate(rows):
    for name, valid_vals in valid_rows.items():
        if is_valid(row, valid_vals):
            if possible.get(name) is None:
                possible[name] = set()
            possible[name].add(i)

# Sort the fields by their number of possible rows
possible = {k: v for k, v in sorted(possible.items(), key=lambda item: len(item[1]))}
# Now map the fields to their row, their's just one for every
class_mapping = {}
taken = set()
for key, possible_childs in possible.items():
    this_item = list(possible_childs - taken)
    this_item = this_item[0]
    taken.add(this_item)
    class_mapping[key] = this_item

# And finally, multiply all fields of your_ticket starting with departure
result_sum = 1
for key, i in class_mapping.items():
    if key.startswith("departure"):
        result_sum *= your_ticket[i]
print(result_sum)
