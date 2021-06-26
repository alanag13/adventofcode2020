from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")


def to_binary_str(input_int):
    return format(input_int, '036b')

def to_int(binary_str):
    return int(binary_str, 2)

class MemoryAssigner:

    def get_assignments(self, input_address, input_value, mask):
        value = to_int(self._apply_mask(to_binary_str(input_value), mask))
        return {input_address: value}

    def _apply_mask(self, binary_str, mask):
        binary_str_list = list(binary_str)
        for i, char in enumerate(mask):
            if char != "X":
                binary_str_list[i] = char
        return "".join(binary_str_list)

class MemoryAssignerV2:
    def get_assignments(self, input_address, input_value, mask):
        addresses = self._apply_mask(to_binary_str(input_address), mask)
        return {"".join(address): input_value for address in addresses}

    def _apply_mask(self, binary_str, mask):
        binary_str_list = list(binary_str)
        addresses = [binary_str_list]

        for i, char in enumerate(mask):
            if char == "1":
                binary_str_list[i] = char

        for i, char in enumerate(mask):
            if char == "X":
                copies = []
                for address in addresses:
                    address[i] = "0"
                    copy = address[:]
                    copy[i] = "1"
                    copies.append(copy)
                addresses.extend(copies)

        return addresses

class CommandRunner:

    def __init__(self, lines, memory_assigner):
        self._lines = lines
        self._addresses = {}
        self._mask = None
        self._memory_assigner = memory_assigner

    def run(self):
        for line in self._lines:
            parsed_command = line.split(" = ")
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
            assignments = self._memory_assigner.get_assignments(address, input_value, self._mask)
            self._addresses.update(assignments)


with open(input_file) as f:
    input_list = [entry.strip() for entry in f]

    runner_pt_1 = CommandRunner(input_list, MemoryAssigner())
    runner_pt_1.run()
    print(f"Part one: {runner_pt_1.get_memory_sum()}")

    runner_pt_2 = CommandRunner(input_list, MemoryAssignerV2())
    runner_pt_2.run()
    print(f"Part two: {runner_pt_2.get_memory_sum()}")

