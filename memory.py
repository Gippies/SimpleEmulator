from collections import OrderedDict

from checkers import check_is_binary, check_bit_int_size, check_unsigned_bit_int_size
from graphics import GraphicComponentWithValues, GraphicComponent
from settings import SCREEN_WIDTH


class Register(GraphicComponentWithValues):
    def __init__(self, name, x=0, y=0, height=100):
        self.internal_value = 0
        self.output_value = 0
        super().__init__(name, [f'Value: {self.output_value}'], x, y, height=height)

    def __str__(self):
        return str(self.output_value)

    def update_value_label_text(self):
        self.value_labels[0].text = f'Value: {self.output_value}'

    def do_register(self, st, d_bit_int, cl):
        check_bit_int_size(d_bit_int)
        check_is_binary(st, cl)

        if st == 1 and cl == 0:
            self.internal_value = d_bit_int
        elif cl == 1:
            self.output_value = self.internal_value
        self.update_value_label_text()
        return self.output_value


class RAM(GraphicComponent):
    def __init__(self):
        # Note that the register list should be accessed unsigned values
        self.register_dict = OrderedDict()
        super().__init__('RAM', SCREEN_WIDTH * 3 // 4, 100, height=580, sub_components=[])

    def __str__(self):
        register_dict_string = '{'
        for key, value in self.register_dict.items():
            register_dict_string += str(key) + ': ' + str(value) + ', '
        register_dict_string = register_dict_string[:-2] + '}'
        return register_dict_string

    def _sort_register_dict(self):
        self.register_dict = {k: self.register_dict[k] for k in sorted(self.register_dict)}

    def do_ram(self, address_bit_int, st, d_bit_int, cl):
        check_unsigned_bit_int_size(address_bit_int)
        if address_bit_int not in self.register_dict:
            self.register_dict[address_bit_int] = Register('Register', self.x, 600 - (40 * address_bit_int), height=40)
            self.sub_components.append(self.register_dict[address_bit_int])
            self._sort_register_dict()
        return self.register_dict[address_bit_int].do_register(st, d_bit_int, cl)


class CombinedMemory:
    def __init__(self):
        self.a_register = Register('A Register', SCREEN_WIDTH // 2 - (150 // 2), 500)
        self.d_register = Register('D Register', SCREEN_WIDTH // 2 - (150 // 2), 400)
        self.ram = RAM()

    def do_combined_memory(self, a, d, a_star, x_bit_int, cl):
        new_a_register_bit_int = self.a_register.do_register(a, x_bit_int, cl)
        return new_a_register_bit_int, self.d_register.do_register(d, x_bit_int, cl), self.ram.do_ram(new_a_register_bit_int, a_star, x_bit_int, cl)
