from settings import BIT_SIZE


def convert_num_to_bit_list(a):
    """
    Converts an integer to a bit_list, highest bit at 0 e.g. 10 -> [0, ..., 0, 1, 0, 1, 0]
    """
    if a >= 0:
        if a > 2 ** (BIT_SIZE - 1) - 1:
            raise ValueError("Error, tried to convert a number too large for the current BIT_SIZE")
        return [int(x) for x in f'{a:0{BIT_SIZE}b}']
    else:
        if a < -1 * 2 ** (BIT_SIZE - 1):
            raise ValueError("Error, tried to convert a number too small for the current BIT_SIZE")
        return [int(x) for x in bin(a + (1 << BIT_SIZE))[2:]]


def get_zero_bit_list():
    return [0 for _ in range(0, BIT_SIZE)]
