from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

class SeatingSystem:
    def __init__(self, initial_board):
        self._current = initial_board
        self._next =[row[:] for row in initial_board]
        self._length = len(initial_board)
        self._width = len(initial_board[0])

    def get_stable_seat_count(self):
        changed_cells = -1
        occupied = -1
        while changed_cells != 0:
            changed_cells = 0
            occupied = 0
            for row in range(self._length):
                for col in range(self._width):
                    old_symbol = self._current[row][col]
                    if old_symbol == ".":
                        continue

                    new_symbol = self._get_new_symbol(old_symbol, row, col)
                    self._next[row][col] = new_symbol
                    if old_symbol != new_symbol:
                        changed_cells += 1
                    if new_symbol == "#":
                        occupied += 1

            self._current, self._next = self._next, self._current
        return occupied

    def _get_new_symbol(self, old_symbol, row, col):
        new_symbol = old_symbol
        occupied_adjacent_seats = self._get_adjacent_occupied_seat_count(row, col)

        if old_symbol == "L" and occupied_adjacent_seats == 0:
            new_symbol = "#"
        elif old_symbol == "#" and occupied_adjacent_seats >= 4:
            new_symbol = "L"

        return new_symbol

    def _get_adjacent_occupied_seat_count(self, row, col):
        occupied = 0
        min_row = 0 if row == 0 else row - 1
        max_row = row if row == self._length - 1 else row + 1
        min_col = 0 if col == 0 else col - 1
        max_col = col if col == self._width - 1 else col + 1
        for row_check in range(min_row, max_row + 1):
    
            for col_check in range(min_col, max_col + 1):
                if row == row_check and col == col_check:
                    continue
                if self._current[row_check][col_check] == "#":
                    occupied += 1
        return occupied



with open(input_file) as f:
    starting_grid = [list(entry.strip()) for entry in f]
    print(SeatingSystem(starting_grid).get_stable_seat_count())
    
