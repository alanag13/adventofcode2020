from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

# Prompt: given a list input with items in the format:
# A-B X: <password>
# get the number of items in the list where <password>
# contains at least A and at most B instances of X.

def get_parts(row):
    row = row.strip()
    count, char, password = row.split()
    min_count, max_count = count.split('-')
    return int(min_count), int(max_count), char[:-1], password

def check_compliance(row):
    min_count, max_count, char, password = get_parts(row)
    matches = 0
    for i in password:
        if char == i:
            matches += 1
    return min_count <= matches <= max_count


with open(input_file) as f:
    num_good_passwords = 0
    for entry in f:
        if check_compliance(entry):
            num_good_passwords += 1
    print(num_good_passwords)

