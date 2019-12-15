from gates import gate_and, gate_xor, gate_or


def half_adder(a, b):
    high = gate_and(a, b)
    low = gate_xor(a, b)
    return high, low


def full_adder(a, b, c):
    temp_high, temp_low = half_adder(b, c)
    other_temp_high, low = half_adder(a, temp_low)
    high = gate_or(other_temp_high, temp_high)
    return high, low
