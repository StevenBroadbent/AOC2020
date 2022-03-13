with open('aoc_2020_16.in') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    fields, tickets = [], []
    for line in data:
        if 'or' in line:
            fields.append(line)
        elif ',' in line:
            tickets.append(line)


def get_ranges():
    ranges = {}
    for line in fields:  # 'departure location: 27-840 or 860-957'
        line = line.split(': ')  # [  'departure location'    , '27-840 or 860-957' ]
        print(line)
        field = line[0]  # 'departure location'
        line = line[1].split(' or ')
        A, B = line[0].split('-'), line[1].split('-')  # A and B are the "ranges"
        lower = (int(A[0]), int(A[1]))
        upper = (int(B[0]), int(B[1]))
        ranges[field] = (lower, upper)
    return ranges


def find_invalids():
    ranges = get_ranges()
    invalid_nums, valid_tickets = [], []
    for line in tickets:
        line = line.split(',')
        ticket = [int(num) for num in line]
        valid_ticket = True
        for num in ticket:
            valid_num = False
            for f, r in ranges.items():
                a1, b1, a2, b2 = r[0][0], r[0][1], r[1][0], r[1][1]
                if num in range(a1, b1 + 1) or num in range(a2, b2 + 1):
                    valid_num = True
                    break
            if not valid_num:
                invalid_nums.append(num)
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(ticket)

    return sum(invalid_nums), valid_tickets


find_invalids()
