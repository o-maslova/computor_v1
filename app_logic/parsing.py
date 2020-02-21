import re
from app_logic.Monomial import Monomial


def define_degree(equation: list):
    """
    In this function the degree of the polynomial is found.
    :param equation_parts: dictionary of the monomials from both parts of the equation.
    :return: maximum found value of the degree from both parts.
    """
    max_degree = max([monomial.degree for monomial in equation])
    return max_degree if max_degree != '' else 1


def check_input(string):
    new_equation = "".join(string.split(' ')).lower()
    result = re.findall(r"(^|\D)(\d+\.\d+|\d+)(\*|\D)(x\^\d+|x)", new_equation)
    if len(result) == 0:
        return False
    return True


def polynom_parts_parse(polynom_part: str, change_sign=False):
    i = 0
    lst = []
    # alpha = ''
    monomial = Monomial()
    lst.append(monomial)
    while i < len(polynom_part):
        if polynom_part[i] in '+-':
            if i != 0:
                monomial = Monomial()
                lst.append(monomial)
            monomial.sign = polynom_part[i] if polynom_part[i] is '-' else '+'
        elif polynom_part[i].isdigit() or polynom_part[i] is '.':
            monomial.first = True if i == 0 else monomial.first
            monomial.number += polynom_part[i]
        elif polynom_part[i].isalpha():
            # alpha = polynom_part[i] if alpha is '' else alpha
            # if polynom_part[i] != alpha:
            #     return "Error"
            monomial.unknown = polynom_part[i]
        elif polynom_part[i] == '^':
            i += 1
            monomial.number = '1' if monomial.number is '' else monomial.number
            monomial.degree = polynom_part[i]
        monomial.change_sign = True if change_sign is True else False
        i += 1
    return lst


def parser(equation: str):
    new_equation = "".join(equation.split(' ')).lower()
    polynomial = []
    equation_parts = new_equation.split('=')
    if len(equation_parts) != 2:
        output = "Wrong format of equation!"
        return output
    polynomial += polynom_parts_parse(equation_parts[0])
    polynomial += polynom_parts_parse(equation_parts[1], change_sign=True)
    alpha = ''
    for i in range(len(polynomial)):
        if i == 0:
            alpha = polynomial[i].unknown
        if polynomial[i].unknown != alpha:
            return None
    return polynomial
