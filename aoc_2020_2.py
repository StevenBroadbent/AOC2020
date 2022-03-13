# https://adventofcode.com/2020/day/2


with open('aoc_2020_2.in') as f:
    records = f.read().split('\n')

part_one_total, part_two_total = 0, 0

for record in records:
    rng, ch, pw = record.split()[0], record.split()[1][0], record.split()[2]
    min_count, max_count = map(int, (rng.split('-')[:2]))
    if pw.count(ch) in range(min_count, max_count + 1):
        part_one_total += 1
    at_index_one = (pw[min_count - 1] == ch)
    at_index_two = (pw[max_count - 1] == ch)
    if at_index_one ^ at_index_two:
        part_two_total += 1

print("total for part one is {}".format(part_one_total))
print("total for part two is {}".format(part_two_total))
assert (part_one_total == 572)
assert (part_two_total == 306)
