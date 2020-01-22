from checkers import check_bit_list_length, check_is_binary
from gates import gate_and, gate_not


def select(s, a_1, a_0):
    check_is_binary(s, a_1, a_0)
    return a_1 if s == 1 else a_0


def select_bit_list(s, a_1_list, a_0_list):
    check_bit_list_length(a_1_list, a_0_list)
    result_list = []
    for i in range(0, len(a_1_list)):
        result_list.append(select(s, a_1_list[i], a_0_list[i]))
    return result_list


def switch(s, a):
    c_1 = gate_and(s, a)
    c_0 = gate_and(gate_not(s), a)
    return c_1, c_0
