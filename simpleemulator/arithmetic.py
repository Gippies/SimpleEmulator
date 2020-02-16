from simpleemulator.checkers import check_is_binary, check_bit_int_size
from simpleemulator.gates import gate_and, gate_xor, gate_or
from settings import MAX_BIT_INT, MIN_BIT_INT


def half_adder(a, b):
    high = gate_and(a, b)
    low = gate_xor(a, b)
    return high, low


def full_adder(a, b, c):
    temp_high, temp_low = half_adder(b, c)
    other_temp_high, low = half_adder(a, temp_low)
    high = gate_or(other_temp_high, temp_high)
    return high, low


def multi_adder(a_bit_int, b_bit_int, c=0):
    check_bit_int_size(a_bit_int, b_bit_int)
    check_is_binary(c)

    answer = a_bit_int + b_bit_int
    if answer > MAX_BIT_INT:
        answer = MIN_BIT_INT + (answer - MAX_BIT_INT - 1)
    return answer


def increment_bit_int(a_bit_int):
    return multi_adder(a_bit_int, 1)


def subtract_bit_ints(a_bit_int, b_bit_int):
    return multi_adder(a_bit_int, -b_bit_int)


def equal_zero_bit_int(a_bit_int):
    check_bit_int_size(a_bit_int)
    return int(a_bit_int == 0)


def is_negative_bit_int(a_bit_int):
    check_bit_int_size(a_bit_int)
    return int(a_bit_int < 0)
