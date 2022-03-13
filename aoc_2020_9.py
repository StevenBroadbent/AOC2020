# aoc 2020 day 9

def two_sum(val, lst):
    for x in lst:
        for y in lst:
            if x + y == val:
                return True
    return False


prelude_len = 25

with open("aoc_2020_9.in") as f:
    data = f.readlines()

data = list(map(int, data))

part_one_answer = 0
for idx in range(prelude_len, len(data)):
    preceding = data[(idx - prelude_len):   idx]
    if not two_sum(data[idx], preceding):
        part_one_answer = data[idx]
        break

print("Part one answer is ", part_one_answer)

pt2 = []
def part2(d):
    for x in range(len(d) - 1):
        for y in range(1, len(d)):
            if sum(d[x:y]) == part_one_answer and x != y:
                return [min(d[x:y]), max(d[x:y])]


pt2 = part2(data)

print("Part two answer is  ", sum(pt2))
assert(part_one_answer == 85848519)
assert(sum(pt2) == 13414198)