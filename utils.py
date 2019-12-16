from checkers import check_bit_list_length, check_is_binary
from settings import BIT_SIZE


def convert_num_to_bit_list(a):
    """
    Converts an integer to a bit_list, highest bit at 0 e.g. 10 -> [0, ..., 0, 1, 0, 1, 0]
    """
    if a >= 0:
        if a > 2 ** BIT_SIZE - 1:
            raise ValueError("Error, tried to convert a number too large for the current BIT_SIZE")
        return [int(x) for x in f'{a:0{BIT_SIZE}b}']
    else:
        if a < -1 * 2 ** (BIT_SIZE - 1):
            raise ValueError("Error, tried to convert a number too small for the current BIT_SIZE")
        return [int(x) for x in bin(a + (1 << BIT_SIZE))[2:]]


def convert_bit_list_to_num(a_list):
    """
    Converts an unsigned bit_list to an integer
    """
    check_bit_list_length(a_list)
    reverse_a_list = a_list[::-1]
    result = 0
    for i, value in enumerate(reverse_a_list):
        check_is_binary(value)
        if value == 1:
            result += 2 ** i
    return result


def get_zero_bit_list():
    return [0 for _ in range(0, BIT_SIZE)]
