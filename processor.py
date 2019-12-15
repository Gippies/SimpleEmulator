from arithmetic import multi_adder
from gates import gate_not_bit_list, gate_and_bit_lists
from plumbing import select_bit_list
from utils import get_zero_bit_list


def u_alu(z, n, d_list):
    z_select = select_bit_list(z, get_zero_bit_list(), d_list)
    return select_bit_list(n, gate_not_bit_list(z_select), z_select)


def alu(z_x, n_x, z_y, n_y, f, n_o, x_list, y_list):
    u_alu_x = u_alu(z_x, n_x, x_list)
    u_alu_y = u_alu(z_y, n_y, y_list)
    x_plus_y = multi_adder(u_alu_x, u_alu_y)
    x_and_y = gate_and_bit_lists(u_alu_x, u_alu_y)
    output_list = select_bit_list(f, x_plus_y, x_and_y)
    return select_bit_list(n_o, gate_not_bit_list(output_list), output_list)
