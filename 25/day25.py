from aocd import get_data
lines = get_data(day=25, year=2020).splitlines()

lines2 = ["5764801", "17807724"]
card1_pub, card2_pub = [int(line) for line in lines]


def transform(subject, loopsize):
    value = 1
    for i in range(loopsize):
        value *= subject
        value = value % 20201227
    return value


def reverse_transform(result, subject):
    loopsize = 0
    while result != 1:
        while result % subject != 0:
            result += 20201227
        result = result / subject
        loopsize += 1
    return loopsize


loopsize1 = reverse_transform(card1_pub, 7)
#loopsize2 = reverse_transform(card2_pub, 7)

key1 = transform(card2_pub, loopsize1)
#key2 = transform(card1_pub, loopsize2)
#assert key1 == key2

print(key1)
