from gates import gate_and, gate_xor, gate_or
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


def multi_adder(a_list, b_list, c):
    if len(a_list) != len(b_list):
        raise ValueError('Error, Tried to multi_add to binary numbers of different length')
    s_list = []
    high = c
    for i in range(0, len(a_list)):
        high, temp_low = full_adder(a_list[i], b_list[i], high)
        s_list.append(temp_low)
    # s_list.append(high)
    return s_list


def increment(a_list):
    return multi_adder(a_list, convert_num_to_bit_list(1), 0)


print(increment(convert_num_to_bit_list(65534)))
