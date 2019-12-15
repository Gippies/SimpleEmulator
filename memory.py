from checkers import check_is_binary
from gates import gate_not, gate_and
"""
Since memory requires a loop in logic gates (which is not possible in programming),
I'm storing the values in actual variables.
"""


class Latch:
    stored_value = 0

    def do_latch(self, st, d):
        check_is_binary(st, d)
        if st == 1:
            self.stored_value = d
        return self.stored_value


class FlipFlop:
    latch_1 = Latch()
    latch_2 = Latch()

    def do_flipflop(self, st, d, cl):
        not_cl = gate_not(cl)
        st_and = gate_and(st, not_cl)
        latch_1_value = self.latch_1.do_latch(st_and, d)
        return self.latch_2.do_latch(cl, latch_1_value)
