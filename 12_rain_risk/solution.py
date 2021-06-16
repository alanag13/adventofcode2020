from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

MOVES = ["W", "N", "E", "S"]
TURNS = ["L", "R"]

class Navigator:
    def __init__(self):
        self._ns_pos = 0
        self._ew_pos = 0
        self._facing_idx = 2

    def handle_command(self, action, amount):
        if action in TURNS:
            self._turn(action, amount)
        else:
            self._move(action, amount)

    def get_manhattan_distance(self):
        return (abs(self._ew_pos) + abs(self._ns_pos))

    def _turn(self, action, amount):
        if action == "L":
            self._facing_idx = (self._facing_idx - (int(amount) // 90)) % 4
        elif action == "R":
            self._facing_idx = (self._facing_idx + (int(amount) // 90)) % 4

    def _move(self, action, amount):
        if action == "F":
            self._move(MOVES[self._facing_idx], amount)
        elif action == "E":
            self._ew_pos += int(amount)
        elif action == "N":
            self._ns_pos += int(amount)
        elif action == "W":
            self._ew_pos -= int(amount)
        elif action == "S":
            self._ns_pos -= int(amount)


with open(input_file) as f:
    facing_idx = 0
    input_list = [entry.strip() for entry in f]
    nav = Navigator()
    for command in input_list:
        action = command[0]
        amount = command[1:]
        nav.handle_command(action, amount)
    print(nav.get_manhattan_distance())
