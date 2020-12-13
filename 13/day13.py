import math
from pathlib import Path
from aocd import get_data
lines = get_data(day=13, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

# lines = [line.replace("L","#") for line in lines]

current_time = int(lines[0])
buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]

next_bus = {}

for bus in buses:
    bus_stop = bus
    while(bus_stop < current_time):
        bus_stop += bus
    next_bus[bus] = bus_stop - current_time

best_bus = min(next_bus, key=next_bus.get)
print(best_bus*next_bus[best_bus])


# Part B
buses = []
elems = []
for i, bus in enumerate(lines[1].split(",")):
    if bus == "x":
        continue
    buses.append(int(bus))
    elems.append(i)


def iterate_timestamp(expected_time):
    for i, bus in enumerate(buses):
        if expected_time % bus == 0:
            if i+1 == len(elems):
                return True
            else:
                expected_time += elems[i+1] - elems[i]
        else:
            return False


max_index = buses.index(max(buses))
i = math.floor(100000000000000/buses[max_index])
#i = 0
result = False
while result is False:
    i += 1
    expected_time = i * buses[max_index] - elems[max_index]
    result = iterate_timestamp(expected_time)

print(expected_time)
