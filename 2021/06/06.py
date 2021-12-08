from collections import Counter
from aocd import get_data

inp = get_data(day=6, year=2021)

init_fishes = [int(itm) for itm in inp.split(",")]


def run(fishes, days):
    fishes = Counter(fishes)
    for _ in range(days):
        new_fishes = Counter()
        for day in fishes:
            if day == 0:
                new_fishes[6] += fishes[day]
                new_fishes[8] += fishes[day]
            else:
                new_fishes[day - 1] += fishes[day]
        fishes = new_fishes
    return fishes


print("---Part A---")
fishes = run(init_fishes, 80)
print(sum(fishes.values()))

print("---Part B---")
fishes = run(init_fishes, 256)
print(sum(fishes.values()))
