from aocd import get_data
inp = get_data(day=23, year=2020)

#inp = "389125467"
cups = [int(char) for char in inp]


def get_next(current, linked, num=3):
    els = []
    for i in range(num):
        current = linked[current]
        els.append(current)
    return els, linked[current]


def get_current_list_str(linked, start=1):
    val = linked[start]
    res = str(start)
    while val != start:
        res += str(val)
        val = linked[val]
    return res


def move_with_linked(linked, current):
    move_els, after_move_el = get_next(current, linked)
    dest = current
    while dest in move_els or dest == current:
        dest -= 1
        if dest < 1:
            dest = len_cups
    linked[current] = after_move_el
    linked[move_els[2]] = linked[dest]
    linked[dest] = move_els[0]
    return linked


def run(linked, iterations):
    active_i = cups[0]
    for i in range(iterations):
        linked = move_with_linked(linked, active_i)
        active_i = linked[active_i]
    return linked


linked_base = {}
for i, el in enumerate(cups):
    if i == len(cups) - 1:
        break
    linked_base[el] = cups[i + 1]

## PART A
linked = linked_base.copy()
len_cups = max(cups)
linked[el] = cups[0]

linked = run(linked, 100)
print(get_current_list_str(linked)[1:])

## PART B
linked = linked_base.copy()
len_cups = int(1e6)
linked[el] = max(cups) + 1
for i in range(max(cups) + 1, len_cups):
    linked[i] = i + 1
linked[len_cups] = cups[0]

linked = run(linked, int(10e6))
print(linked[1] * linked[linked[1]])
