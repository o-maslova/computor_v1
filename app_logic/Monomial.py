class Monomial:
    first = False
    sign = '+'
    number = ''
    degree = ''
    unknown = ''
    show_degree = True
    is_float = False
    change_sign = False

    def __str__(self):
        if self.first is True and self.sign is '+':
            output = f"{self.number}"
        else:
            output = f"{self.sign} {self.number}"
        if self.unknown != '':
            output = output + ' * ' if self.number != '' else output
            output += f"{self.unknown}"
        if self.degree != '' and self.show_degree is True:
            output += f"^{self.degree}"
        return output

    def create_monomial(self):
        if self.unknown != '' and self.degree == '':
            self.degree = '1'
            self.show_degree = False
        elif self.unknown == '' and self.number != '':
            self.degree = '0'
            self.show_degree = False
        if '.' in self.number:
            self.is_float = True
        if self.change_sign:
            self.sign = '+' if self.sign == '-' else '-'
