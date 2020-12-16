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

while len(buses) != 1:
    offset1, bus1 = buses[-1]
    offset2, bus2 = buses[-2]
    i = 0
    while bus1 != bus2:
        number = bus1 * i + offset1
        if (number - offset2) % bus2 == 0:
            break
        i += 1
    # Replace last two buses by their equivalent
    buses = buses[:-2]
    buses.append((number, bus1 * bus2))

print(buses[0][1] - buses[0][0])
