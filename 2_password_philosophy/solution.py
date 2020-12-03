from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def get_parts(row):
    row = row.strip()
    indexes, char, password = row.split()
    first_pos, last_pos = indexes.split('-')
    return int(first_pos), int(last_pos), char[:-1], password

def check_part_one_compliance(row):
    min_count, max_count, char, password = get_parts(row)
    matches = 0
    for i in password:
        if char == i:
            matches += 1
    return min_count <= matches <= max_count

def check_part_two_compliance(row):
    first_pos, last_pos, char, password = get_parts(row)
    first_match = password[first_pos - 1] == char
    last_match = password[last_pos - 1] == char
    return first_match != last_match

with open(input_file) as f:
    part_one_good_passwords = 0
    part_two_good_passwords = 0
    for entry in f:
        if check_part_one_compliance(entry):
            part_one_good_passwords += 1
        if check_part_two_compliance(entry):
            part_two_good_passwords += 1

    print(f"Part one: {part_one_good_passwords}")
    print(f"Part two: {part_two_good_passwords}")