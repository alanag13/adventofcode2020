from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

# Prompt: get the product of the three numbers in the input
# that add up to 2020

checked = set()
with open(input_file) as f:
    for entry in f:
        entry = int(entry.strip())
        for item in checked:
            prev = 2020 - (entry + item)
            if prev in checked:
                print(f"{entry} * {item} * {prev} = {entry * item * prev}")
                exit()
        checked.add(entry)