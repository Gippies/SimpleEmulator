from checkers import check_is_binary, check_bit_int_size, check_unsigned_bit_int_size
from settings import BIT_SIZE


class Register:
    def __init__(self):
        self.internal_value = 0
        self.output_value = 0

    def do_register(self, st, d_bit_int, cl):
        check_bit_int_size(d_bit_int)
        check_is_binary(st, cl)

        if st == 1 and cl == 0:
            self.internal_value = d_bit_int
        elif cl == 1:
            self.output_value = self.internal_value
        return self.output_value


class RAM:
    def __init__(self):
        print(f"Allocating {2 * 2 ** BIT_SIZE} bytes of RAM...")
        # Note that the register list should be accessed unsigned values
        self.register_list = []
        for i in range(0, 2 ** BIT_SIZE):
            self.register_list.append(Register())
        print("RAM allocated")

    def do_ram(self, address_bit_int, st, d_bit_int, cl):
        check_unsigned_bit_int_size(address_bit_int)
        return self.register_list[address_bit_int].do_register(st, d_bit_int, cl)


class CombinedMemory:
    def __init__(self):
        self.a_register = Register()
        self.d_register = Register()
        self.ram = RAM()

    def do_combined_memory(self, a, d, a_star, x_bit_int, cl):
        new_a_register_bit_int = self.a_register.do_register(a, x_bit_int, cl)
        return new_a_register_bit_int, self.d_register.do_register(d, x_bit_int, cl), self.ram.do_ram(new_a_register_bit_int, a_star, x_bit_int, cl)
