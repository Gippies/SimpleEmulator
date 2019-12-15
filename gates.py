from checkers import check_is_binary, check_bit_list_length


def gate_not(a):
    check_is_binary(a)
    return int(not a)


def gate_not_bit_list(a_list):
    check_bit_list_length(a_list)
    return [gate_not(x) for x in a_list]


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


def gate_and_bit_list(a_list):
    """
    ANDs all the values together in an a_list
    """
    if len(a_list) == 1:
        return a_list[0]
    else:
        half = len(a_list) // 2
        return gate_and(gate_and_bit_list(a_list[:half]), gate_and_bit_list(a_list[half:]))


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
