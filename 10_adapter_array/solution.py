from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

diff_count = {1: 0, 2: 0, 3: 0}
distinct_arrangements = 0

def get_num_combintations_ending_with(num, input_dict):
    return input_dict.get(num - 1, 0) \
        + input_dict.get(num - 2, 0) \
        + input_dict.get(num - 3, 0)

with open(input_file) as f:
    input_list = sorted([int(entry.strip()) for entry in f])
    input_dict = {0: 1}
    input_dict.update({item: 0 for item in input_list})
    input_dict[input_list[-1] + 3] = 0

    prev_item = 0
    for key in input_dict:
        if prev_item:
            diff_count[key - prev_item] += 1  
        else:
            diff_count[key] = 1     

        if key:
            input_dict[key] = get_num_combintations_ending_with(key, input_dict)  
            distinct_arrangements = input_dict[key]

        prev_item = key

    print (f"Part one: {diff_count[1] * diff_count[3]}")
    print (f"Part two: {distinct_arrangements}")