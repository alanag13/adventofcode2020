from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def get_seat(row, col):
    return (row * 8) + col

def get_seat_from_boarding_pass(boarding_pass):
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[-3:].replace("L", "0").replace("R", "1"), 2)
    return get_seat(row, col)

with open(input_file) as f:
    max_seat_id = 0
    my_seat_id = None
    seats = {get_seat_from_boarding_pass(entry.strip()) for entry in f}
    for row in range(128):
        for col in range(8):
            seat_id = get_seat(row, col)
            if seat_id > max_seat_id and seat_id in seats:
                max_seat_id = seat_id

            if not my_seat_id \
                and seat_id not in seats \
                and seat_id - 1 in seats \
                and seat_id + 1 in seats:
                    my_seat_id = seat_id
    
    print(f"Part one: {max_seat_id}")
    print(f"Part two: {my_seat_id}")