from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def _get_rule_ranges(rule_desc):
    range_descs = rule_desc.split(" or ")
    ranges = []
    for desc in range_descs:
        txt_range = desc.split("-")
        int_range = [int(x) for x in txt_range]
        ranges.append(int_range)
    return ranges

def _is_valid_for_rules(value, rules):
    for rule in rules.values():
        for rule_range in rule:
            if rule_range[0] <= int(value) <= rule_range[1]:
                return True

    return False

def _get_field_map(valid_tickets, rules):
    wip_position_map = {}
    for name, ranges in rules.items():
        rule = {name: ranges}
        wip_position_map[name] = [idx for idx in range(len(rules)) 
                                    if all([_is_valid_for_rules(ticket[idx], rule) for ticket in valid_tickets])]

    final_position_map = {}
    for name, options in sorted(wip_position_map.items(), key=lambda item: len(item[1])):
        indexes = [idx for idx in options if idx not in final_position_map]
        if (len(indexes) == 1):
            final_position_map[indexes[0]] = name

    return final_position_map


with open(input_file) as f:
    rules = {}
    nearby_tickets = []
    your_ticket = None
    do_your_ticket = False
    do_nearby_tickets = False

    for entry in f:
        line = entry.strip()
        if not line:
            continue

        if entry.startswith("your ticket:"):
            do_your_ticket = True
            continue
        
        if entry.startswith("nearby tickets:"):
            do_nearby_tickets = True
            continue

        if do_nearby_tickets:
            nearby_tickets.append(line.split(","))
        elif do_your_ticket:
            your_ticket = line.split(",")
        else:
            rule_parts = line.split(":")
            rule_ranges = _get_rule_ranges(rule_parts[1])
            rules[rule_parts[0]] = rule_ranges

    invalid_fields = [int(val) for ticket in nearby_tickets
                               for val in ticket if not _is_valid_for_rules(val, rules)]

    valid_tickets = [ticket for ticket in nearby_tickets 
                        if all([_is_valid_for_rules(val, rules) for val in ticket])]

    field_map = _get_field_map(valid_tickets, rules)
    pt_two_result = 1
    for idx, field in field_map.items():
        if field.startswith("departure"):
            pt_two_result *= int(your_ticket[idx])

    print(f"Part one: {sum(invalid_fields)}")
    print(f"Part two: {pt_two_result}")