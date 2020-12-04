from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def validate_range(lower, upper, value):
    is_number = value.isdigit()
    if not is_number:
        return False

    return lower <= int(value) <= upper

def is_hex(value):
    try:
        int(value, 16)
        return True
    except:
        pass

def validate_height(value):
    if not len(value) > 2:
        return False

    valid = False
    units = value[-2:]
    measure = value[:-2]
    if units == "cm":
        valid = validate_range(150, 193, measure)
    elif units == "in":
        valid = validate_range(59, 76, measure)

    return valid

def part_one_check_validity(fields):
    return (len(fields) >= 8 or (len(fields) == 7 and "cid" not in fields))

def part_two_check_validity(fields):
    if not part_one_check_validity(fields):
        return False

    hgt_field = fields["hcl"]
    pid_field = fields["pid"]

    return validate_range(1920, 2002, fields["byr"]) \
        and validate_range(2010, 2020, fields["iyr"]) \
        and validate_range(2020, 2030, fields["eyr"]) \
        and validate_height(fields["hgt"]) \
        and hgt_field[0] == "#" and len(hgt_field) == 7 and is_hex(hgt_field[1:]) \
        and fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} \
        and len(pid_field) == 9 and pid_field.isdigit()

def check_validity(fields):
    return part_one_check_validity(fields), part_two_check_validity(fields)

with open(input_file) as f:
    fields = {}
    part_one_valid_passports = 0
    part_two_valid_passports = 0

    for entry in f:
        entry = entry.strip()
        if not entry:
            one, two = check_validity(fields)
            part_one_valid_passports += one
            part_two_valid_passports += two
            fields = {}
            continue
        fields.update({pair.split(":")[0]: pair.split(":")[1] for pair in entry.split()})
    
    # check if the very last entry was valid
    one, two = check_validity(fields)
    part_one_valid_passports += one
    part_two_valid_passports += two

    print(f"Part one: {part_one_valid_passports}")
    print(f"Part two: {part_two_valid_passports}")