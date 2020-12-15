import math
from pathlib import Path
from aocd import get_data
lines = get_data(day=13, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

current_time = int(lines[0])
buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

next_bus = {}

for bus in buses:
    bus_stop = bus
    while(bus_stop < current_time):
        bus_stop += bus
    next_bus[bus] = bus_stop - current_time

best_bus = min(next_bus, key=next_bus.get)
print(best_bus * next_bus[best_bus])


# Part B
buses = []
for i, bus in enumerate(lines[1].split(",")):
    if bus == "x":
        continue
    buses.append((i, int(bus)))

buses = sorted(buses, key=lambda x: x[1], reverse=True)
max_offset, max_bus = buses[0]
# Remove first element as we store it seperately
buses.pop(0)
min_offset, _ = buses[-1]


i = math.floor(100000000000000 / max_bus)
#i = 0
result = False
while result is False:
    i += 1
    expected_time = i * max_bus - max_offset
    for offset, bus in buses:
        if (expected_time + offset) % bus != 0:
            break
        elif offset == min_offset:
            result = True
            break

print(expected_time)
