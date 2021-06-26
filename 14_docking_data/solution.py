from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

def parse_command(command):
    parts = command.split(" = ")
    return parts

def to_binary_str(input_int):
    return format(input_int, '036b')

def to_int(binary_str):
    return int(binary_str, 2)

def apply_mask(binary_str, mask):
    binary_str_list = list(binary_str)
    for i, char in enumerate(mask):
        if char != "X":
            binary_str_list[i] = char
    return "".join(binary_str_list)

class CommandRunner:

    def __init__(self, lines):
        self._lines = lines
        self._addresses = {}
        self._mask = None

    def run(self):
        for line in self._lines:
            parsed_command = parse_command(line)
            self._run_command(parsed_command)

    def get_memory_sum(self):
        result = 0
        for key in self._addresses:
            result += self._addresses[key]
        return result

    def _run_command(self, parsed_command):
        if parsed_command[0] == "mask":
            self._mask = parsed_command[1]
        else:
            input_value = int(parsed_command[1])
            address = int(parsed_command[0].split("[")[1].strip("]"))
            value = to_int(apply_mask(to_binary_str(input_value), self._mask))
            self._addresses[address] = value


with open(input_file) as f:
    input_list = [entry.strip() for entry in f]
    runner = CommandRunner(input_list)
    runner.run()
    print(runner.get_memory_sum())

