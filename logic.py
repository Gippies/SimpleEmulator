from gates import gate_not_bit_list
from plumbing import select_bit_list
from utils import get_zero_bit_list


def u_alu(z, n, d_list):
    z_select = select_bit_list(z, get_zero_bit_list(), d_list)
    return select_bit_list(n, gate_not_bit_list(z_select), z_select)
