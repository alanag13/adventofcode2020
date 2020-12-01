from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "inputs", "input.txt")

checked = set()
with open(input_file) as f:
    for line in f:
        line = int(line.strip())
        diff = 2020 - line
        if diff in checked:
            print(f"{line} * {diff} = {line * diff}")
            exit()
        checked.add(line)