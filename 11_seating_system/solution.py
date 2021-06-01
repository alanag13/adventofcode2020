from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

class Seat:
    def __init__(self, value):
        self.values = [value, None]
        self.neighbors = None

class SeatUpdater:
    def __init__(self, grid, neighbors_func, min_occupied_to_trigger_empty):
        self._grid = grid
        self._round = 0
        self._length = len(self._grid)
        self._width = len(self._grid[0])
        initialize_neighbors(self._grid, self._length, self._width, neighbors_func)
        self._min_occupied_to_trigger_empty = min_occupied_to_trigger_empty

    def get_stable_seat_count(self):
        changed_cells = True
        occupied = 0
        while changed_cells:
            changed_cells, occupied = self._update()
        
        return occupied

    def _update(self):
        updated = False
        cur_idx = self._round % 2
        next_idx = (self._round + 1) % 2
        occupied = 0
        for row in range(self._length):
            for col in range(self._width):
                seat = self._grid[row][col]
                if seat:
                    values = seat.values
                    value = values[cur_idx]
                    next_val = self._get_next_value(seat.neighbors, value, cur_idx)
                    values[next_idx] = next_val

                    if not updated:
                        updated = value != next_val

                        if not updated and value == "#":
                            occupied += 1

        self._round += 1

        return updated, occupied

    def _get_next_value(self, neighbors, cur_value, cur_idx):
        occupied_neighbors = sum(1 for n in neighbors if n.values[cur_idx] == "#")
        next_val = cur_value
        if cur_value == "#" and occupied_neighbors >= self._min_occupied_to_trigger_empty:
            next_val = "L"
        elif cur_value == "L" and not occupied_neighbors:
            next_val = "#"
        return next_val

def initialize_neighbors(grid, length, width, neighbors_func):
    max_row = length - 1
    max_col = width - 1
    for row in range(length):
        for col in range(width):
            cell = grid[row][col]
            if cell:
                cell.neighbors = neighbors_func(grid, row, col, max_row, max_col)

def get_adjacent_neighbors(grid, row_idx, col_idx, max_row, max_col):
    min_row = max(0, row_idx - 1)
    max_row = min(row_idx + 1, max_row)
    min_col = max(0, col_idx - 1)
    max_col = min(col_idx + 1, max_col)
    return get_visible_neighbors(grid, row_idx, col_idx, max_row, max_col, min_row=min_row, min_col=min_col)


def get_visible_neighbors(grid, row_idx, col_idx, max_row, max_col, min_row=0, min_col=0):
    neighbors = []
    for row_inc in range(-1, 2):
        for col_inc in range(-1, 2):
            if row_inc == 0 and col_inc == 0:
                continue
            seat = _get_first_visible_seat(grid, row_idx, col_idx, max_row, min_row, max_col, min_col, row_inc, col_inc)
            if seat:
                neighbors.append(seat)

    return neighbors


def _get_first_visible_seat(grid, row_idx, col_idx, max_row, min_row, max_col, min_col, inc_row, inc_col):
    seat = None
    while True:
        row_idx += inc_row
        col_idx += inc_col
        if not (min_row <= row_idx <= max_row) or not (min_col <= col_idx <= max_col):
            return None
        seat = grid[row_idx][col_idx]
        if seat:
            break

    return seat


with open(input_file) as f:
    seat_grid = []
    second_grid = []

    for entry in f:
        seat_grid.append([Seat(cell) if cell != "." else None for cell in list(entry.strip())])
        second_grid.append([Seat(cell) if cell != "." else None for cell in list(entry.strip())])

    print(f"Part one: {SeatUpdater(seat_grid, get_adjacent_neighbors, 4).get_stable_seat_count()}")
    print(f"Part two: {SeatUpdater(second_grid, get_visible_neighbors, 5).get_stable_seat_count()}")
