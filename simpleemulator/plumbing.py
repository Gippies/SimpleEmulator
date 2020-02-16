from simpleemulator.checkers import check_is_binary, check_bit_int_size, check_unsigned_bit_int_size
from simpleemulator.gates import gate_and, gate_not


def select(s, a_1, a_0):
    check_is_binary(s, a_1, a_0)
    return a_1 if s == 1 else a_0


def select_bit_int(s, a_1_bit_int, a_0_bit_int):
    check_bit_int_size(a_1_bit_int, a_0_bit_int)
    check_is_binary(s)
    return a_1_bit_int if s == 1 else a_0_bit_int


def select_unsigned_bit_int(s, a_1_bit_int, a_0_bit_int):
    check_unsigned_bit_int_size(a_1_bit_int, a_0_bit_int)
    check_is_binary(s)
    return a_1_bit_int if s == 1 else a_0_bit_int


def switch(s, a):
    c_1 = gate_and(s, a)
    c_0 = gate_and(gate_not(s), a)
    return c_1, c_0
