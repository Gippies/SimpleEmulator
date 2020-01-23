# BIT_SIZE should be a number 2^n. E.g. 8, 16, 32, 64 etc.
# Though, it is recommended to just leave this as 16.
BIT_SIZE = 16

MAX_BIT_INT = 2 ** (BIT_SIZE - 1) - 1
MAX_UNSIGNED_BIT_INT = 2 ** BIT_SIZE - 1
MIN_BIT_INT = -1 * 2 ** (BIT_SIZE - 1)
