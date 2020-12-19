from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

rolling_sum = 0
contiguous_nums = []
PART_ONE_SOLUTION = 70639851

def has_sum_pair_in_range(input_list, value, start, end):
    checked = set()
    for i in range(start, end):
        item = input_list[i]
        diff = value - item
        if diff in checked:
            return True
        checked.add(item)

with open(input_file) as f:
    input_list = [int(entry.strip()) for entry in f]
    for i in range(len(input_list)):
        num = input_list[i]
        if i > 24 and not has_sum_pair_in_range(input_list, num, i - 25, i):
            print(f"Part one: {num}")
        
        if len(contiguous_nums) > 1 and rolling_sum == PART_ONE_SOLUTION:
            print(f"Part two: {min(contiguous_nums) + max(contiguous_nums)}")
            exit()

        contiguous_nums.append(num)
        rolling_sum += num

        while rolling_sum > PART_ONE_SOLUTION:
            remove = contiguous_nums[0]
            rolling_sum -= remove
            contiguous_nums.remove(remove)