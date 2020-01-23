from checkers import check_is_binary, check_bit_int_size
from utils import convert_num_to_bit_list


def gate_not(a):
    check_is_binary(a)
    return int(not a)


def gate_not_bit_int(a_bit_int):
    check_bit_int_size(a_bit_int)
    return ~a_bit_int


def gate_nand(a, b):
    """
    Returns NAND of two bits.
    """
    check_is_binary(a, b)
    return int(not (a and b))


def gate_and(a, b):
    """
    Returns AND of two bits.
    """
    check_is_binary(a, b)
    return int(a and b)


def gate_and_bit_int_into_one(a_bit_int):
    """
    ANDs all the bits in the provided integer together
    """
    check_bit_int_size(a_bit_int)
    # TODO: This could be optimized to just use an if statement
    a_list = convert_num_to_bit_list(a_bit_int)
    answer = a_list[0]
    for i in range(1, len(a_list)):
        answer = gate_and(answer, a_list[i])
    return answer


def gate_and_bit_ints(a_bit_int, b_bit_int):
    """
    ANDs each bit together between the integers
    """
    check_bit_int_size(a_bit_int, b_bit_int)
    return a_bit_int & b_bit_int


def gate_or(a, b):
    """
    Returns OR of two bits.
    """
    check_is_binary(a, b)
    return int(a or b)


def gate_xor(a, b):
    """
    Returns XOR of two bits.
    """
    check_is_binary(a, b)
    return int(a ^ b)
