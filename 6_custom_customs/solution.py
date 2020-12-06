from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

with open(input_file, "a") as f:
    # make sure the very last batch of input gets processed
    f.write("\n")

with open(input_file) as f:
    individual_yes_count = 0
    group_yes_count = 0
    unique_letters = {}
    group_size = 0
    for entry in f:
        entry = entry.strip()
        if not entry:
            individual_yes_count += len(unique_letters)
            for item in unique_letters:
                if unique_letters[item] == group_size:
                    group_yes_count += 1
            group_size = 0
            unique_letters = {}
        else:
            group_size += 1
            for char in entry:
                letter_total = unique_letters.get(char) or 0
                unique_letters[char] = letter_total + 1

    print(f"Part one: {individual_yes_count}")
    print(f"Part two: {group_yes_count}")