from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")


def get_pt_one_bus_id_and_time(bus_ids, start_time):
    while True:
        for idx in bus_ids:
            bus_id = bus_ids[idx]
            if not start_time % bus_id:
                return bus_id, start_time
        start_time += 1

def get_pt_two_timestamp(bus_ids):
    current_timestamp = 0
    increase_factor = 1
    
    for offset in bus_ids:
        bus_id = bus_ids[offset]

        while True:
            if not ((current_timestamp + offset) % bus_id):
                break
            current_timestamp += increase_factor
        
        # note: this only works because every bus id is prime.
        # If it were not prime we would need to break down the bus id into each of its prime multiples
        # and then only multiply by them if those multiples hadn't already been used earlier
        increase_factor *= bus_id

    return current_timestamp


with open(input_file) as f:
    input_list = [entry.strip() for entry in f]
    pt_one_start_time = int(input_list[0])
    bus_ids = {idx: int(bus_id) for idx, bus_id in enumerate(input_list[1].split(",")) if bus_id != "x"}
    print(bus_ids)
    bus_id, time = get_pt_one_bus_id_and_time(bus_ids, pt_one_start_time)
    pt_two_time = get_pt_two_timestamp(bus_ids)
    print(bus_id * (time - pt_one_start_time))
    print(pt_two_time)
