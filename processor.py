from arithmetic import multi_adder
from checkers import check_is_binary, check_bit_int_size, check_unsigned_bit_int_size
from gates import gate_not_bit_int, gate_and_bit_ints, gate_or, gate_not
from memory import CombinedMemory
from plumbing import select_bit_int, select_unsigned_bit_int
from utils import convert_unsigned_int_to_bit_list


def u_alu(z, n, d_bit_int):
    check_is_binary(z, n)
    check_bit_int_size(d_bit_int)

    answer = d_bit_int
    if z == 1:
        answer = 0
    if n == 1:
        answer = ~answer
    return answer


def alu(z_x, n_x, z_y, n_y, f, n_o, x_bit_int, y_bit_int):
    u_alu_x = u_alu(z_x, n_x, x_bit_int)
    u_alu_y = u_alu(z_y, n_y, y_bit_int)
    x_plus_y = multi_adder(u_alu_x, u_alu_y)
    x_and_y = gate_and_bit_ints(u_alu_x, u_alu_y)
    output_list = select_bit_int(f, x_plus_y, x_and_y)
    return select_bit_int(n_o, gate_not_bit_int(output_list), output_list)


def condition(lt, eq, gt, x_bit_int):
    check_is_binary(lt, eq, gt)
    check_bit_int_size(x_bit_int)

    if lt == 1 and x_bit_int < 0:
        return 1
    if eq == 1 and x_bit_int == 0:
        return 1
    if gt == 1 and x_bit_int > 0:
        return 1
    return 0


def instruction_decoder(x_bit_int):
    check_unsigned_bit_int_size(x_bit_int)
    x_list = convert_unsigned_int_to_bit_list(x_bit_int)

    ci = x_list[0]
    w_bit_int = select_unsigned_bit_int(ci, 0, x_bit_int)
    ci_select = convert_unsigned_int_to_bit_list(select_unsigned_bit_int(ci, x_bit_int, 0))

    reverse_ci_select = ci_select[::-1]
    temp_a = reverse_ci_select[5]

    a = gate_or(gate_not(ci), temp_a)
    return (
        ci, reverse_ci_select[12], reverse_ci_select[11], reverse_ci_select[10],
        reverse_ci_select[9], reverse_ci_select[8], reverse_ci_select[7],
        reverse_ci_select[6], a, reverse_ci_select[4], reverse_ci_select[3],
        reverse_ci_select[2], reverse_ci_select[1], reverse_ci_select[0], w_bit_int
    )


class ControlUnit:
    def __init__(self):
        self.memory = CombinedMemory()

    def do_control_unit(self, i_bit_int, cl):
        ci, sm, zx, nx, zy, ny, f, no, a, d, a_star, gt, eq, lt, x_bit_int = instruction_decoder(i_bit_int)
        check_is_binary(ci)

        if ci == 1:
            a_register_value, d_register_value, a_ram_value = self.memory.do_combined_memory(0, 0, 0, x_bit_int, cl)
            y_bit_int = select_bit_int(sm, a_ram_value, a_register_value)
            alu_result = alu(zx, nx, zy, ny, f, no, d_register_value, y_bit_int)
            a_register_value, d_register_value, a_ram_value = self.memory.do_combined_memory(a, d, a_star, alu_result, cl)
            j = condition(lt, eq, gt, alu_result)
            return j, a_register_value, d_register_value, a_ram_value
        else:
            a_register_value, d_register_value, a_ram_value = self.memory.do_combined_memory(a, d, a_star, x_bit_int, cl)
            y_bit_int = select_bit_int(sm, a_ram_value, a_register_value)
            alu_result = alu(zx, nx, zy, ny, f, no, d_register_value, y_bit_int)
            j = condition(lt, eq, gt, alu_result)
            return j, a_register_value, d_register_value, a_ram_value
