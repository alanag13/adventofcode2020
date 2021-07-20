from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def calc(grouped_equation_arr):
    rolling_sum = 0
    i = 0
    while i < len(grouped_equation_arr) - 2:
        first, op, second = rolling_sum or grouped_equation_arr[i], grouped_equation_arr[i+1], grouped_equation_arr[i+2]
        if type(first) == list:
            first = calc(first)
        if type(second) == list:
            second = calc(second)

        if op == "+":
            rolling_sum = (int(first) + int(second))
        elif op == "*":
            rolling_sum = (int(first) * int(second))

        i += 2
    return rolling_sum


def group_terms(equation_arr):
    parens = 0
    terms = []
    expression = []

    for char in equation_arr:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

        expression.append(char)
        
        if parens == 0:
            if len(expression) == 1:
                terms.append(expression[0])
            else:
                terms.append(group_terms(expression[1:len(expression)-1]))
            expression = []

    return terms



with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]
    part_one = 0
    for line in lines:
        parts = []
        for part in line.split(" "):
            parts.extend(list(part))
        answer = calc(group_terms(parts))
        part_one += answer
    print(part_one)
