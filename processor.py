from arithmetic import multi_adder, is_negative_bit_list, equal_zero_bit_list
from gates import gate_not_bit_list, gate_and_bit_lists, gate_or, gate_and, gate_not
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


def condition(lt, eq, gt, x_list):
    is_x_neg = is_negative_bit_list(x_list)
    is_x_zero = equal_zero_bit_list(x_list)
    return gate_or(gate_or(gate_and(lt, is_x_neg), gate_and(eq, is_x_zero)), gate_and(gt, gate_and(gate_not(is_x_neg), gate_not(is_x_zero))))


def instruction_decoder(x_list):
    ci = x_list[0]
    w = select_bit_list(ci, get_zero_bit_list(), x_list)
    ci_select = select_bit_list(ci, x_list, get_zero_bit_list())

    reverse_ci_select = ci_select[::-1]
    temp_a = reverse_ci_select[5]

    a = gate_or(gate_not(ci), temp_a)
    return (
        reverse_ci_select[12], reverse_ci_select[11], reverse_ci_select[10],
        reverse_ci_select[9], reverse_ci_select[8], reverse_ci_select[7],
        reverse_ci_select[6], a, reverse_ci_select[4], reverse_ci_select[3],
        reverse_ci_select[2], reverse_ci_select[1], reverse_ci_select[0], w
    )
