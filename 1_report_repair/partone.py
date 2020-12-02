from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

# Prompt: get the product of the two numbers in the input
# that add up to 2020

checked = set()
with open(input_file) as f:
    for entry in f:
        entry = int(entry.strip())
        diff = 2020 - entry
        if diff in checked:
            print(f"{entry} * {diff} = {entry * diff}")
            exit()
        checked.add(entry)