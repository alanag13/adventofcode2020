from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

# Prompt: given a list input with items in the format:
# A-B X: <password>
# get the number of items in the list where <password>
# contains X at exactly one of either position A or position B,
# where the first character of <password> is position 1.

def get_parts(row):
    row = row.strip()
    count, char, password = row.split()
    first_pos, last_pos = count.split('-')
    return int(first_pos) - 1, int(last_pos) - 1, char[:-1], password

def check_compliance(row):
    first_pos, last_pos, char, password = get_parts(row)
    first_match = password[first_pos] == char
    last_match = password[last_pos] == char
    return first_match != last_match

with open(input_file) as f:
    num_good_passwords = 0
    for entry in f:
        if check_compliance(entry):
            num_good_passwords += 1
    print(num_good_passwords)