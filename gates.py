def _check_is_binary(*args):
    for a in args:
        if a not in (0, 1):
            raise ValueError('Error, variable is not a bit')


def gate_nand(a, b):
    """
    Returns NAND of two bits.
    """
    _check_is_binary(a, b)
    return not (a and b)


def gate_and(a, b):
    """
    Returns AND of two bits.
    """
    _check_is_binary(a, b)
    return a and b


def gate_or(a, b):
    """
    Returns OR of two bits.
    """
    _check_is_binary(a, b)
    return a or b


def gate_xor(a, b):
    """
    Returns XOR of two bits.
    """
    _check_is_binary(a, b)
    return a ^ b
