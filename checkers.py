from settings import BIT_SIZE


def check_is_binary(*args):
    for a in args:
        if a not in (0, 1):
            raise ValueError('Error, variable is not a bit')


def check_bit_list_length(*args):
    for bit_list in args:
        if len(bit_list) != BIT_SIZE:
            raise ValueError('Error, bit list length is not the BIT_SIZE')
