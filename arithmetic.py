from checkers import check_bit_list_length, check_is_binary
from gates import gate_and, gate_xor, gate_or, gate_not_bit_list, gate_and_bit_list_into_one
from utils import convert_num_to_bit_list


def half_adder(a, b):
    high = gate_and(a, b)
    low = gate_xor(a, b)
    return high, low


def full_adder(a, b, c):
    temp_high, temp_low = half_adder(b, c)
    other_temp_high, low = half_adder(a, temp_low)
    high = gate_or(other_temp_high, temp_high)
    return high, low


def multi_adder(a_list, b_list, c=0):
    check_bit_list_length(a_list, b_list)

    s_list = []
    high = c
    # A bit list has the highest bit at 0. So need to go in reverse through them. Starts at len - 1 and ends at 0.
    for i in range(len(a_list) - 1, -1, -1):
        high, temp_low = full_adder(a_list[i], b_list[i], high)
        s_list.insert(0, temp_low)
    # s_list.insert(0, high)  - This is where the last carry would go.
    return s_list


def increment_bit_list(a_list):
    return multi_adder(a_list, convert_num_to_bit_list(1))


def subtract_bit_list(a_list, b_list):
    """
    Does a - b
    """
    negative_b_list = increment_bit_list(gate_not_bit_list(b_list))
    return multi_adder(a_list, negative_b_list)


def equal_zero_bit_list(a_list):
    # TODO: This can be simplified to just check for zeros
    check_bit_list_length(a_list)
    return gate_and_bit_list_into_one(gate_not_bit_list(a_list))


def is_negative_bit_list(a_list):
    """
    If the most significant bit is 1, then the binary number is negative
    """
    check_is_binary(a_list[0])
    return a_list[0]
