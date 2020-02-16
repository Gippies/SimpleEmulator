from simpleemulator.utils.graphics import GraphicView, GraphicComponentWithValues
from simpleemulator.processor import ControlUnit
from settings import CLOCK_STEP_MODE, SCREEN_WIDTH
from simpleemulator.utils.conversions import convert_bit_list_to_num


class Program(GraphicComponentWithValues):
    def __init__(self, file_path):
        self.instructions = []
        self.current_address = 0
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
                    self.instructions.append(convert_bit_list_to_num(instruction_bit_list))
        print("Program loaded")
        value_texts = []
        for index, v in enumerate(self.instructions):
            bin_v = bin(v)[2:]
            if index == self.current_address:
                value_texts.append('->' + bin_v)
            else:
                value_texts.append(bin_v)
        super().__init__('Program', value_texts, SCREEN_WIDTH // 4, 100, height=580)

    def update_value_label_text(self):
        for index, v in enumerate(self.instructions):
            bin_v = bin(v)[2:]
            if index == self.current_address:
                self.value_labels[index].text = '->' + bin_v
            else:
                self.value_labels[index].text = bin_v

    def get_current_address(self):
        return self.current_address

    def set_current_address(self, new_addr):
        self.current_address = new_addr
        self.update_value_label_text()

    def increment_current_address(self):
        self.set_current_address(self.current_address + 1)

    def get_current_instruction(self):
        return self.instructions[self.current_address]

    def num_of_instructions(self):
        return len(self.instructions)


class Computer(GraphicView):
    def __init__(self):
        self.control_unit = ControlUnit()
        self.program = None
        self.is_first_run = True
        self.is_running = True
        super().__init__('Computer', [self.control_unit.memory.a_register, self.control_unit.memory.d_register, self.control_unit.memory.ram])

    def _run_program_on_control_unit(self, clock):
        current_address = self.program.get_current_address()
        print(f"Current clock value: {clock}")
        print(f"Current program address: {current_address}")
        if current_address >= self.program.num_of_instructions() or current_address < 0:
            print(f"\nReached program address {current_address} which is outside the allocated program (from 0 to {self.program.num_of_instructions() - 1} inclusive)")
            print(f"Shutting Down Emulator...")
            self.is_running = False
        else:
            j, a_register_value, d_register_value, a_ram_value = self.control_unit.do_control_unit(self.program.get_current_instruction(), clock)
            if j == 1 and clock == 1:
                self.program.set_current_address(a_register_value)
            elif clock == 1:
                self.program.increment_current_address()
            print(f"Returned condition value: {j}")
            print(f"Returned register A value: {a_register_value}")
            print(f"Returned register D value: {d_register_value}")
            print(f"Returned RAM value: {a_ram_value}")
            print(f"All RAM values: {self.control_unit.memory.ram}\n")

    def on_click(self):
        if self.is_running:
            if CLOCK_STEP_MODE:
                self.do_computer()
            else:
                while self.is_running:
                    self.do_computer()
        else:
            print("Computer has already terminated.")

    def do_computer(self):
        # Performs one clock cycle
        if self.is_first_run:
            if self.program.num_of_instructions() == 0:
                raise ValueError("Error, tried to start computer without a program loaded")
            print("Executing program...")
            self.is_first_run = False
        self._run_program_on_control_unit(0)
        if self.is_running:
            self._run_program_on_control_unit(1)

    def load_program(self, program):
        self.program = program
        self.sub_components.append(self.program)
