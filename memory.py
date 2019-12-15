from checkers import check_is_binary, check_bit_list_length
from gates import gate_not, gate_and
from settings import BIT_SIZE

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
