from checkers import check_bit_list_length
from gates import gate_and, gate_not, gate_or


def select(s, a_1, a_0):
    # TODO: This can be simplified to just use a condition
    a_1_and = gate_and(s, a_1)
    a_0_and = gate_and(gate_not(s), a_0)
    return gate_or(a_1_and, a_0_and)


def select_bit_list(s, a_1_list, a_0_list):
    # TODO: This can be simplified to just use a condition
    check_bit_list_length(a_1_list, a_0_list)
    result_list = []
    for i in range(0, len(a_1_list)):
        result_list.append(select(s, a_1_list[i], a_0_list[i]))
    return result_list


def switch(s, a):
    c_1 = gate_and(s, a)
    c_0 = gate_and(gate_not(s), a)
    return c_1, c_0
