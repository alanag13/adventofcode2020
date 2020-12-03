from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def check_for_part_one_match(entry, checked):
    diff = 2020 - entry
    if diff in checked:
        return entry, diff

def check_for_part_two_match(entry, checked):
    for item in checked:
        prev = 2020 - (entry + item)
        if prev in checked:
            return entry, item, prev

checked = set()
with open(input_file) as f:
    for entry in f:
        entry = int(entry.strip())
        pair = check_for_part_one_match(entry, checked)
        triple = check_for_part_two_match(entry, checked)

        if pair:
            first, second = pair
            print(f"Part one: {first * second}")

        if triple:
            first, second, third = triple
            print(f"Part two: {first * second * third}")

        checked.add(entry)