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


def check_input(string: str):
    """
    In this function the input string is checking for the first time via regular expression
    to define whether the input string corresponds to the equation format.
    :param string: input string.
    :return: True if the string corresponds to the format, False in other case.
    """
    new_equation = "".join(string.split(' ')).lower()
    result = re.findall(r"(^|\D)(\d*\.\d*|\d*)(\**|\D)([a-z]\^\d*|[a-z])", new_equation)
    if len(result) == 0:
        return False
    return True


def polynom_parts_parse(polynom_part: str, change_sign=False):
    i = 0
    lst = []
    monomial = Monomial()
    lst.append(monomial)
    while i < len(polynom_part):
        if polynom_part[i] in '+-':
            if i != 0:
                monomial = Monomial()
                lst.append(monomial)
            monomial.sign = polynom_part[i]
        elif polynom_part[i].isdigit() or polynom_part[i] is '.':
            monomial.first = True if i == 0 else monomial.first
            monomial.number += polynom_part[i]
        elif polynom_part[i].isalpha():
            monomial.unknown = polynom_part[i]
        elif polynom_part[i] == '^':
            i += 1
            monomial.number = '1' if monomial.number is '' else monomial.number
            monomial.degree = polynom_part[i]
        elif polynom_part[i] in "?/,&%$#@!()><\"\'\{\}:;[]":
            return "Error"
        monomial.change_sign = True if change_sign is True else False
        i += 1
    return lst


def parser(equation: str):
    new_equation = "".join(equation.split(' ')).lower()
    polynomial = []
    equation_parts = new_equation.split('=')
    if len(equation_parts) != 2 or len(equation_parts[0]) == 0 or len(equation_parts[1]) == 0:
        return None
    for i in range(len(equation_parts)):
        change_sign = False if i == 0 else True
        tmp = polynom_parts_parse(equation_parts[i], change_sign=change_sign)
        if tmp == "Error":
            return None
        polynomial += tmp
    unknowns = [elem.unknown for elem in polynomial if elem.unknown != '']
    for alpha in unknowns:
        if alpha != unknowns[0]:
            return None
    return polynomial
