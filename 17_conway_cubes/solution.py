from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

class MultiDimensionConway:
    def __init__(self, dimensions, active_cubes):
        self._dimensions = dimensions
        self._cur_active = active_cubes
        self._next_active = None
        self._neighbor_diffs = self._get_neighbor_coord_diff_list()

    def get_active_cubes(self):
        return self._cur_active

    def next_turn(self):
        relevant_inactive_cells = set()
        self._next_active = set()

        for coords in self._cur_active:
            neighbors = self._get_neighbors(coords)
            active = self._get_active_cells(neighbors)

            for cell in self._get_inactive_cells(neighbors):
                relevant_inactive_cells.add(cell)

            if len(active) in [2,3]:
                self._next_active.add(coords)

        for cell in relevant_inactive_cells:
            neighbors = self._get_neighbors(cell)
            active = self._get_active_cells(neighbors)

            if len(active) == 3:
                self._next_active.add(cell)

        self._cur_active = self._next_active


    def _get_active_cells(self, cells):
        return {cell for cell in cells if cell in self._cur_active}

    def _get_inactive_cells(self, cells):
        active_cells = self._get_active_cells(cells)
        return {cell for cell in cells if cell not in active_cells}

    def _get_neighbors(self, coords):
        neighbors = set()
        for diff in self._neighbor_diffs:
            neighbor_coords = tuple([mod + coord for mod, coord in zip(diff, coords)])
            if neighbor_coords != coords:
                neighbors.add(neighbor_coords)

        return neighbors

    def _get_neighbor_coord_diff_list(self):
        diffs = [tuple([-1, 0, 1])] * self._dimensions
        results = [[]]
        for diff in diffs:
            results = [result + [mod] for result in results for mod in diff]

        return results


with open(input_file) as f:
    lines = [list(line.strip()) for line in f.readlines()]
    init_3d_cubes = set()
    init_4d_cubes = set()
    
    for i in range(len(lines)):
        for k in range(len(lines[i])):
            if lines[i][k] == "#":
                init_3d_cubes.add((k,i,0))
                init_4d_cubes.add((k,i,0,0))

    pt_one_conway_game = MultiDimensionConway(3, init_3d_cubes)
    pt_two_conway_game = MultiDimensionConway(4, init_4d_cubes)

    for _ in range(6):
        pt_one_conway_game.next_turn()
        pt_two_conway_game.next_turn()

    print(len(pt_one_conway_game.get_active_cubes()))
    print(len(pt_two_conway_game.get_active_cubes()))