from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

MOVES = ["W", "N", "E", "S"]
TURNS = ["L", "R"]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, amount):
        if direction == "E":
            self.x += int(amount)
        elif direction == "N":
            self.y += int(amount)
        elif direction == "W":
            self.x -= int(amount)
        elif direction == "S":
            self.y -= int(amount)

    def rotate(self, direction, amount):
        rotations = int(amount) // 90

        if direction == "L":
            rotations = (rotations * -1) % 4

        for _ in range(rotations):
            x = self.x
            y = self.y

            self.x = y
            self.y = x * -1


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
        self._ship_loc = Point(0, 0)
        self._facing_idx = 2

    def get_manhattan_distance(self):
        return (abs(self._ship_loc.x) + abs(self._ship_loc.y))

    def turn(self, action, amount):
        offset = int(amount) // 90
        if action == "L":
            offset *= -1
        self._facing_idx = (self._facing_idx + offset) % 4

    def move(self, action, amount):
        if action == "F":
            self.move(MOVES[self._facing_idx], amount)
        else:
            self._ship_loc.move(action, amount)


class WaypointMovementHandler:

    def __init__(self):
        self._waypoint = Point(10, 1)
        self._ship_loc = Point(0, 0)

    def get_manhattan_distance(self):
        return (abs(self._ship_loc.x) + abs(self._ship_loc.y))

    def turn(self, action, amount):
        self._waypoint.rotate(action, amount)

    def move(self, action, amount):
        if action == "F":
            self._ship_loc.y += (self._waypoint.y * int(amount))
            self._ship_loc.x += (self._waypoint.x * int(amount))
        else:
            self._waypoint.move(action, amount)


with open(input_file) as f:
    input_list = [entry.strip() for entry in f]
    ship_nav = Navigator(ShipMovementHandler())
    waypoint_nav = Navigator(WaypointMovementHandler())
    for command in input_list:
        action = command[0]
        amount = command[1:]
        ship_nav.handle_command(action, amount)
        waypoint_nav.handle_command(action, amount)
    print(f"Part one: {ship_nav.get_manhattan_distance()}")
    print(f"Part two: {waypoint_nav.get_manhattan_distance()}")
