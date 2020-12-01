from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "inputs", "input.txt")

checked = set()
with open(input_file) as f:
    for line in f:
        line = int(line.strip())

        for item in checked:
            prev = 2020 - (line + item)
            if prev in checked:
                print(f"{line} * {item} * {prev} = {line * item * prev}")
                exit()
        checked.add(line)