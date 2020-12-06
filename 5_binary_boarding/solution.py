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
    seats = set()
    max_seat_id = None
    min_seat_id = None
    seat_id_sum = 0
    for entry in f:
        entry = entry.strip()
        seat_id = get_seat_from_boarding_pass(entry)
        if max_seat_id is None or seat_id > max_seat_id:
            max_seat_id = seat_id
        if min_seat_id is None or seat_id < min_seat_id:
            min_seat_id = seat_id
        seats.add(seat_id)
        seat_id_sum += seat_id
    
    range_sum = sum(range(min_seat_id, max_seat_id + 1))
    my_seat_id = range_sum - seat_id_sum
    
    print(f"Part one: {max_seat_id}")
    print(f"Part two: {my_seat_id}")