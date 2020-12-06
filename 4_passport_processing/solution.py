from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def validate_range(lower, upper, value):
    return value.isdigit() and (lower <= int(value) <= upper)

def is_hex(value):
    int(value, 16)
    return True

def validate_height(value):
    units = value[-2:]
    measure = value[:-2]
    if units == "cm":
        return validate_range(150, 193, measure)
    elif units == "in":
        return validate_range(59, 76, measure)
    return False

def has_required_fields(fields):
    return (len(fields) >= 8 or (len(fields) == 7 and "cid" not in fields))

def validate_fields(fields):
    try:
        hcl = fields["hcl"]
        pid = fields["pid"]

        return validate_range(1920, 2002, fields["byr"]) \
            and validate_range(2010, 2020, fields["iyr"]) \
            and validate_range(2020, 2030, fields["eyr"]) \
            and validate_height(fields["hgt"]) \
            and hcl[0] == "#" and len(hcl) == 7 and is_hex(hcl[1:]) \
            and fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} \
            and len(pid) == 9 and pid.isdigit()
    except:
        return False

with open(input_file, "a") as f:
    # make sure the very last batch of input gets processed
    f.write("\n")

with open(input_file) as f:
    part_one_valid_passports = 0
    part_two_valid_passports = 0
    fields = {}
    for entry in f:
        entry = entry.strip()
        if not entry:
            if has_required_fields(fields):
                part_one_valid_passports += 1
                part_two_valid_passports += validate_fields(fields)
            fields = {}
        else:
            fields.update({pair.split(":")[0]: pair.split(":")[1] for pair in entry.split()})

    print(f"Part one: {part_one_valid_passports}")
    print(f"Part two: {part_two_valid_passports}")