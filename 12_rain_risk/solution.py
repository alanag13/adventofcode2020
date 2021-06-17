from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

MOVES = ["W", "N", "E", "S"]
TURNS = ["L", "R"]

class Navigator:
    def __init__(self, movement_handler):
        self._movement_handler = movement_handler

    def get_manhattan_distance(self):
        return self._movement_handler.get_manhattan_distance()

    def handle_command(self, action, amount):
        if action in TURNS:
            self._movement_handler.turn(action, amount)
        else:
            self._movement_handler.move(action, amount)

class ShipMovementHandler:

    def __init__(self):
        self._ns_pos = 0
        self._ew_pos = 0
        self._facing_idx = 2

    def get_manhattan_distance(self):
        return (abs(self._ew_pos) + abs(self._ns_pos))

    def turn(self, action, amount):
        if action == "L":
            self._facing_idx = (self._facing_idx - (int(amount) // 90)) % 4
        elif action == "R":
            self._facing_idx = (self._facing_idx + (int(amount) // 90)) % 4

    def move(self, action, amount):
        if action == "F":
            self.move(MOVES[self._facing_idx], amount)
        elif action == "E":
            self._ew_pos += int(amount)
        elif action == "N":
            self._ns_pos += int(amount)
        elif action == "W":
            self._ew_pos -= int(amount)
        elif action == "S":
            self._ns_pos -= int(amount)


class WaypointMovementHandler:

    def __init__(self):
        self._wp_ns_pos = 1
        self._wp_ew_pos = 10
        self._ns_pos = 0
        self._ew_pos = 0

    def get_manhattan_distance(self):
        return (abs(self._ew_pos) + abs(self._ns_pos))

    def turn(self, action, amount):
        rotations = int(amount) // 90

        if action == "L":
            rotations = (rotations * -1) % 4

        for _ in range(rotations):
            wp_ew_pos = self._wp_ew_pos
            wp_ns_pos = self._wp_ns_pos

            self._wp_ew_pos = wp_ns_pos
            self._wp_ns_pos = wp_ew_pos * -1

    def move(self, action, amount):
        if action == "F":
            self._ns_pos += (self._wp_ns_pos * int(amount))
            self._ew_pos += (self._wp_ew_pos * int(amount))
        elif action == "E":
            self._wp_ew_pos += int(amount)
        elif action == "N":
            self._wp_ns_pos += int(amount)
        elif action == "W":
            self._wp_ew_pos -= int(amount)
        elif action == "S":
            self._wp_ns_pos -= int(amount)


with open(input_file) as f:
    input_list = [entry.strip() for entry in f]
    ship_nav = Navigator(ShipMovementHandler())
    waypoint_nav = Navigator(WaypointMovementHandler())
    for command in input_list:
        action = command[0]
        amount = command[1:]
        ship_nav.handle_command(action, amount)
        waypoint_nav.handle_command(action, amount)
    print(ship_nav.get_manhattan_distance())
    print(waypoint_nav.get_manhattan_distance())
