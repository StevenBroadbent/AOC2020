with open("aoc_2020_6.in") as input_file:
    input_data = input_file.read()


data = [d.replace('\n', '') for d in input_data.split('\n\n')]

group_yes_totals = [len(set(d)) for d in data]
print("Part one answer is {}".format(sum(group_yes_totals)))

# part two..
input_data = [d.replace('\n', '-') for d in input_data.split('\n\n')]

answers = []
for group in input_data:
    ppl = group.split('-')
    set_list = [set(x) for x in ppl if x]
    if len(ppl) == 1:
        answers.append(len(set_list[0]))
        continue
    final_set = set_list[0]
    u = set.intersection(*set_list)
    answers.append(len(u))

print("Part two answer is {}".format(sum(answers)))
assert (sum(answers) == 3570)
