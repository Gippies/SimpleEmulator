from processor import ControlUnit
from utils import convert_bit_list_to_num


class Computer:
    def __init__(self):
        self.control_unit = ControlUnit()
        self.program = []
        self.program_current_address = 0

    def _run_program_on_control_unit(self, clock):
        if self.program_current_address >= len(self.program) or self.program_current_address < 0:
            raise ValueError(f"Error, tried to access program address {self.program_current_address} which doesn't exist")
        j, a_register_value = self.control_unit.do_control_unit(self.program[self.program_current_address], clock)
        if j == 1 and clock == 1:
            self.program_current_address = convert_bit_list_to_num(a_register_value)
        elif clock == 1:
            self.program_current_address += 1
        print(f"A register value: {a_register_value}")
        print(f"Current program address: {self.program_current_address}")

    def do_computer(self):
        # Performs one clock cycle
        if len(self.program) == 0:
            raise ValueError("Error, tried to run the computer without a program loaded")
        while True:
            self._run_program_on_control_unit(1)
            self._run_program_on_control_unit(0)

    def load_program(self, file_path):
        print("Loading program...")
        with open(file_path, 'r') as in_file:
            for line in in_file:
                instruction_bit_list = []
                for c in line:
                    if c != '\n':
                        instruction_bit_list.append(int(c))
                self.program.append(instruction_bit_list)
        print("Program Loaded, Executing...")
