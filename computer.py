from processor import ControlUnit
from settings import CLOCK_STEP_MODE
from utils import convert_bit_list_to_num


class Computer:
    def __init__(self):
        self.control_unit = ControlUnit()
        self.program = []
        self.program_current_address = 0
        self.is_running = True

    def _run_program_on_control_unit(self, clock):
        print(f"Current clock value: {clock}")
        print(f"Current program address: {self.program_current_address}")
        if self.program_current_address >= len(self.program) or self.program_current_address < 0:
            print(f"\nReached program address {self.program_current_address} which is outside the allocated program (from 0 to {len(self.program) - 1} inclusive)")
            print(f"Shutting Down Emulator...")
            self.is_running = False
        else:
            j, a_register_value, d_register_value, a_ram_value = self.control_unit.do_control_unit(self.program[self.program_current_address], clock)
            if j == 1 and clock == 1:
                self.program_current_address = a_register_value
            elif clock == 1:
                self.program_current_address += 1
            print(f"Returned condition value: {j}")
            print(f"Returned register A value: {a_register_value}")
            print(f"Returned register D value: {d_register_value}")
            print(f"Returned RAM value: {a_ram_value}")
            print(f"All RAM values: {self.control_unit.memory.ram}\n")

    def do_computer(self):
        # Performs one clock cycle
        if len(self.program) == 0:
            raise ValueError("Error, tried to run the computer without a program loaded")
        print("Executing program...")
        while self.is_running:
            if CLOCK_STEP_MODE:
                input("Press Enter to continue...")
            self._run_program_on_control_unit(0)
            if self.is_running:
                self._run_program_on_control_unit(1)

    def load_program(self, file_path):
        print("Loading program...")
        with open(file_path, 'r') as in_file:
            for line in in_file:
                instruction_bit_list = []
                for c in line:
                    if c == '0' or c == '1':
                        instruction_bit_list.append(int(c))
                    elif c == '#':
                        break
                if len(instruction_bit_list) > 0:
                    self.program.append(convert_bit_list_to_num(instruction_bit_list))
        print("Program loaded")
