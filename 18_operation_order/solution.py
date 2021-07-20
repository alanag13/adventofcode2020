from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def calc(math_tokens, op_order):
    answer = 0
  
    for op_group in op_order:
        i = 1
        while i < len(math_tokens):
            first, op, second = math_tokens[i-1], math_tokens[i], math_tokens[i+1]

            if op not in op_group:
                i += 2
                continue

            if type(first) == list:
                first = calc(first, op_order)
            if type(second) == list:
                second = calc(second, op_order)

            if op == "+":
                answer = (int(first) + int(second))
            else:
                answer = (int(first) * int(second))

            math_tokens = math_tokens[:i-1] + [answer] + math_tokens[i+2:]

    return answer


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
        
        if parens:
            continue

        new_term = expression[0] if len(expression) == 1 else group_terms(expression[1:len(expression)-1])
        terms.append(new_term)
        expression = []

    return terms



with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]
    part_one = 0
    part_two = 0
    for line in lines:
        parts = []
        for part in line.split(" "):
            parts.extend(list(part))
        part_one += calc(group_terms(parts), ["+*"])
        part_two += calc(group_terms(parts), ["+", "*"])
    print(f"Part one: {part_one}")
    print(f"Part two: {part_two}")
