from settings import BIT_SIZE


def check_is_binary(*args):
    for a in args:
        if a not in (0, 1):
            raise ValueError(f'Error, variable is: {a} but should be 0 or 1')


def check_bit_list_length(*args):
    for bit_list in args:
        if len(bit_list) != BIT_SIZE:
            raise ValueError(f'Error, bit list length is: {len(bit_list)} but should be BIT_SIZE: {BIT_SIZE}')
