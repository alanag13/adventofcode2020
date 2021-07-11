from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

most_recent = None
turn_num = 0

class MemoryGame:
    def __init__(self, starting_numbers, max_turns):
        self._previously_spoken = max_turns*[None]
        self._turn_num = 0
        self._most_recent = None
        self._initialize_game(starting_numbers)

    def get_next_spoken_number(self):
        self._turn_num += 1
        two_most_recent = self._previously_spoken[self._most_recent]
        to_speak = two_most_recent[0] - two_most_recent[1]
        prev = self._previously_spoken[to_speak]

        if prev is None:
            entries = [self._turn_num, self._turn_num]
        else:
            prev[0], prev[1] = prev[1], prev[0]
            prev[0] = self._turn_num
            entries = prev

        self._previously_spoken[to_speak] = entries
        self._most_recent = to_speak
        return to_speak

    def _initialize_game(self, starting_numbers):
        for entry in starting_numbers:
            self._turn_num += 1
            self._previously_spoken[int(entry)] = [self._turn_num, self._turn_num]
            self._most_recent = int(entry)


with open(input_file) as f:
    input_list = f.read().split(",")
    game_one = MemoryGame(input_list, 2020)
    game_two = MemoryGame(input_list, 30000000)
    pt_one_result = None
    pt_two_result = None
    for _ in range(2020 - len(input_list)):
        pt_one_result = game_one.get_next_spoken_number()

    for _ in range(30000000 - len(input_list)):
        pt_two_result = game_two.get_next_spoken_number()

    print(f"Part one: {pt_one_result}")
    print(f"Part two: {pt_two_result}")
