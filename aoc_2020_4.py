import string
required_fields = ["ecl", "eyr", "byr", "iyr", "hgt", "hcl", "pid"]
valid_eye_colours = 'amb blu brn gry grn hzl oth'.split()
part_one_result = 0
hcl_chars = string.ascii_lowercase + string.digits + '#'
units_list = ["in", "cm"]
with open("aoc_2020_4.in") as f:
    all_ps = [term.replace('\n', ' ') for term in f.read().split('\n\n')]


def is_valid_ps(s):
    given_fields = {field.split(":")[0] for field in s.split() if field.split(':')[1]}
    if set(required_fields).issubset(given_fields):
        return True
    return False


for p in all_ps:
    is_valid_ps(p)
part_one_answer = sum(is_valid_ps(s) for s in all_ps)
print("Part one answer is ", part_one_answer)

###########################################################################################
#
#   Part two - forget the previous rules, Santa has new ones!
#
##########################################################################################

'''byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''


def validate_hcl(s):
    is7 = len(s) == 7
    hash_first = s[0] == '#'
    valid_chars = all([ch in hcl_chars for ch in s[1:]])
    return all([valid_chars, is7, hash_first])


def validate_hgt(s):
    if (not s[:2] in string.digits) and s[-2:] not in units_list:
        return False
    hgt, unit = int(s[:-2]), s[-2:]
    if unit == "in" and hgt in range(59, 76 + 1):
        return True
    if unit == "cm" and hgt in range(150, 193 + 1):
        return True
    return False


for p in [term for term in all_ps if is_valid_ps(term)]:
    fields = p.split()
    d = {f.split(":")[0]: f.split(":")[1] for f in fields}
    byr_is_valid = int(d["byr"]) in range(1920, 2002 + 1)
    iyr_is_valid = int(d["iyr"]) in range(2010, 2020 + 1)
    eyr_is_valid = int(d["eyr"]) in range(2020, 2030 + 1)
    cl_is_valid = d["ecl"] in valid_eye_colours
    pid_is_valid = d['pid'].isnumeric and len(d['pid']) == 9
    hcl_is_valid = validate_hcl(d['hcl'])
    hgt_is_valid = validate_hgt(d['hgt'])
    conditions = [byr_is_valid, iyr_is_valid, eyr_is_valid, cl_is_valid,
                  pid_is_valid, hcl_is_valid, hgt_is_valid]
    part_one_result += all(conditions)

print("Part two answer is ", part_one_result)

assert (part_one_answer == 239)
assert (part_one_result == 188)
