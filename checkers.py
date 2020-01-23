from settings import BIT_SIZE, MAX_BIT_INT, MIN_BIT_INT, MAX_UNSIGNED_BIT_INT


def check_is_binary(*args):
    for a in args:
        if a not in (0, 1):
            raise ValueError(f'Error, variable is: {a} but should be 0 or 1')


def check_bit_int_size(*args):
    for num in args:
        if num > MAX_BIT_INT or num < MIN_BIT_INT:
            raise ValueError(f"Error, variable is: {num} but should be between {MIN_BIT_INT} and {MAX_BIT_INT} for {BIT_SIZE}-bit signed numbers")


def check_unsigned_bit_int_size(*args):
    for num in args:
        if num > MAX_UNSIGNED_BIT_INT or num < 0:
            raise ValueError(f"Error, variable is: {num} but should be between 0 and {MAX_UNSIGNED_BIT_INT} for {BIT_SIZE}-bit unsigned numbers")


def check_bit_list_length(*args):
    for bit_list in args:
        if len(bit_list) != BIT_SIZE:
            raise ValueError(f'Error, bit list length is: {len(bit_list)} but should be BIT_SIZE: {BIT_SIZE}')
