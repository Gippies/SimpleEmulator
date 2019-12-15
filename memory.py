from checkers import check_is_binary, check_bit_list_length
from gates import gate_not, gate_and
from plumbing import switch, select_bit_list
from settings import BIT_SIZE
from utils import convert_num_to_bit_list

"""
Since memory requires a loop in logic gates (which is not possible in programming),
I'm storing the values in actual variables.
"""


class Latch:
    def __init__(self):
        self.stored_value = 0

    def do_latch(self, st, d):
        check_is_binary(st, d)
        if st == 1:
            self.stored_value = d
        return self.stored_value


class FlipFlop:
    def __init__(self):
        self.latch_1 = Latch()
        self.latch_2 = Latch()

    def do_flipflop(self, st, d, cl):
        not_cl = gate_not(cl)
        st_and = gate_and(st, not_cl)
        latch_1_value = self.latch_1.do_latch(st_and, d)
        return self.latch_2.do_latch(cl, latch_1_value)


class Register:
    def __init__(self):
        self.flipflop_list = []
        for i in range(0, BIT_SIZE):
            self.flipflop_list.append(FlipFlop())

    def do_register(self, st, d_list, cl):
        check_bit_list_length(d_list)
        flipflop_value_list = []
        for i in range(len(d_list)):
            flipflop_value_list.append(self.flipflop_list[i].do_flipflop(st, d_list[i], cl))
        return flipflop_value_list


class RAM:
    def __init__(self):
        print(f"Allocating {2 * 2 ** BIT_SIZE} bytes of RAM...")
        self.register_list = []
        for i in range(0, 2 ** BIT_SIZE):
            self.register_list.append(Register())
        print("RAM allocated")

    def _get_recursive_switch(self, address_bit_list, st):
        if len(address_bit_list) == 1:
            c_1, c_0 = switch(address_bit_list[0], st)
            result_list = [c_1, c_0]
            return result_list
        else:
            c_1, c_0 = switch(address_bit_list[0], st)
            temp_list_1 = self._get_recursive_switch(address_bit_list[1:], c_1)
            temp_list_1.extend(self._get_recursive_switch(address_bit_list[1:], c_0))
            return temp_list_1

    def _get_recursive_select(self, address_bit_list, register_result_list):
        if len(address_bit_list) == 1:
            return select_bit_list(address_bit_list[0], register_result_list[0], register_result_list[1])
        else:
            half = len(register_result_list) // 2
            return select_bit_list(address_bit_list[0], self._get_recursive_select(address_bit_list[1:], register_result_list[:half]), self._get_recursive_select(address_bit_list[1:], register_result_list[half:]))

    def do_ram(self, address_bit_list, st, d_list, cl):
        stored_address_list = self._get_recursive_switch(address_bit_list, st)
        for i in range(0, len(stored_address_list)):
            if stored_address_list[i] != 0:
                print(f'Stored Address List is {stored_address_list[i]} at {i}')
        register_result_list = []
        for i in range(0, len(self.register_list)):
            register_result_list.append(self.register_list[i].do_register(stored_address_list[i], d_list, cl))
        return self._get_recursive_select(address_bit_list, register_result_list)
