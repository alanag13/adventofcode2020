from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

file_col_width = 31
part_one_instructions = {(3, 1): 0}
part_two_instructions = {
    (1, 1): 0,
    (3, 1): 0,
    (5, 1): 0,
    (7, 1): 0,
    (1, 2): 0
}

def count_hit_trees(entry, row_num, instructions_dict):
    for key in instructions_dict:
        right, down = key
        if not row_num % down:
            adjusted_row_num = int(row_num / down)
            pos = adjusted_row_num * right
            row = entry.strip()
            if row[pos % file_col_width] == "#":
                instructions_dict[key] += 1

with open(input_file) as f:
    row_num = 0
    
    for entry in f:
        count_hit_trees(entry, row_num, part_one_instructions)
        count_hit_trees(entry, row_num, part_two_instructions)
        row_num += 1
    
    print(f"Part one: {part_one_instructions[(3, 1)]}")
 
    result = 1
    for key in part_two_instructions:
        result *= part_two_instructions[key]

    print(f"Part two: {result}")
     
