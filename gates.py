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
    # TODO: Change all the gates to just use nand
    check_is_binary(a, b)
    return int(not (a and b))


def gate_and(a, b):
    """
    Returns AND of two bits.
    """
    check_is_binary(a, b)
    return int(a and b)


def gate_and_bit_list_into_one(a_list):
    """
    ANDs all the values together in an a_list into one bit
    """
    answer = a_list[0]
    for i in range(1, len(a_list)):
        answer = gate_and(answer, a_list[i])
    return answer


def gate_and_bit_lists(a_list, b_list):
    """
    ANDs each bit together between the bit lists
    """
    check_bit_list_length(a_list, b_list)
    return [gate_and(a_list[i], b_list[i]) for i in range(0, len(a_list))]


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
