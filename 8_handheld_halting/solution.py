from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

class Driver:
    
    def __init__(self, program):
        self._program = program
        self._line_count = len(program)
        self._line_num = 0
        self._accumulator = 0
    
    def run(self, instruction):
        visited = {}
        while self._line_num not in visited:
            visited[self._line_num] = instruction
            getattr(self, f"_{instruction[0]}")(int(instruction[1]))
            if self._line_num > self._line_count - 1:
                return True, self._accumulator
            instruction = self._program[self._line_num]
        return False, self._accumulator

    def find_patch(self):
        finished = False
        accumulator = None
        while not finished:
            instruction = self._program[self._line_num]
            prev_accumulator = self._accumulator
            prev_line_num = self._line_num
            cmd = instruction[0]
            param = instruction[1]
            if cmd == "jmp":
                finished, accumulator = self.run(["nop", param])
            elif cmd == "nop":
                finished, accumulator = self.run(["jmp", param])

            if cmd == "jmp" or cmd == "nop":
                self._accumulator = prev_accumulator
                self._line_num = prev_line_num

            getattr(self, f"_{cmd}")(int(param))

        return accumulator

    def _acc(self, increment):
        self._line_num += 1
        self._accumulator += increment

    def _nop(self, dummy):
        self._line_num += 1

    def _jmp(self, offset):
        self._line_num += offset

with open(input_file) as f:
    program = [entry.strip().split() for entry in f]
    finished, accumulator = Driver(program).run(program[0])
    print(f"Part one: {accumulator}")
    accumulator = Driver(program).find_patch()
    print(f"Part two: {accumulator}")
