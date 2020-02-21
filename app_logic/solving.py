def solve_equation(polynomial: dict):
    """ 
        Discriminant formula: b^2 - 4 * a * c
        :param polynomial: dictionary which contain polynomial
        :return: 
    """
    if '2' in polynomial.keys() and polynomial.get('2') != 0:
        polynomial['1'] = 0 if '1' not in polynomial.keys() else polynomial['1']
        polynomial['0'] = 0 if '0' not in polynomial.keys() else polynomial['0']
        try:
            discriminant = polynomial['1'] ** 2 - 4 * polynomial['2'] * polynomial['0']
        except ZeroDivisionError:
            return "There is no solution.", None
        output, details = discriminant_solutions(polynomial, discriminant)
        return output, details
    elif '0' in polynomial.keys() and '1' in polynomial.keys():
        try:
            res = polynomial['0'] * -1 / polynomial['1']
        except ZeroDivisionError:
            return "There is no solution.", None
        details = [f"The root is calculated by the formula: ",
                    "-b / c\n", "Solution: ",
                    f"{str(polynomial['0'] * -1)} / {str(polynomial['1'])}",
                    "Result: ", f"{str(res)}"]
        return f"The solution is:\n{str(round(res, 6))}", details
    elif ('0' in polynomial.keys() and polynomial['0'] == 0) or \
            ('1' in polynomial.keys() and polynomial['1'] == 0):
        return "All the real numbers are solutions.", None
    elif '0' in polynomial.keys() and polynomial['0'] != 0 or \
            ('1' in polynomial.keys() and polynomial['1'] != 0):
        return "There is no solution.", None


def make_details(details, polynomial, square_of_d=False, x_1=False, x_2=False):
    tmp_dict = {'first': ['-', x_1], 'second': ['+', x_2]}
    if square_of_d:
        details += f"Square root of discriminant: ", f"{square_of_d}\n"
        for root_number, params in tmp_dict.items():
            details += f"The {root_number} root is calculated by the formula: ", f"(-b {params[0]} sqrt(D)) / 2a\n"
            details += f"{root_number.title()} solution: ", f"({str((polynomial['1'] * -1))} - {str(square_of_d)}) / 2 * {str(polynomial['2'])}\n"
            details += f"Result: ", f"{params[1]}\n\n"
    else:
        details += f"The solution is found by the formula: ", f"-b / 2a\n"
        details += f"Solution: ", f"{str((polynomial['1'] * -1))} / 2 * {str(polynomial['2'])}\n"
        details += f"Result: ", f"{x_1}\n\n"
    return details


def discriminant_solutions(polynomial: dict, discriminant: float):
    output = ""
    details = ["Discriminant formula: ", "b^2 - 4 * a * c\n", f"Discriminant: ", f"{str(discriminant)}\n\n"]
    if discriminant > 0:
        output += "Discriminant is strictly positive, the two solutions are:\n"
        square_of_d = float(find_square(discriminant))
        x_1 = round((polynomial['1'] * -1 - square_of_d) / (2 * polynomial['2']), 6)
        x_2 = round((polynomial['1'] * -1 + square_of_d) / (2 * polynomial['2']), 6)
        output += f"{str(x_1)}\n"
        output += f"{str(x_2)}\n"
        make_details(details=details, polynomial=polynomial, square_of_d=square_of_d, x_1=x_1, x_2=x_2)
    elif discriminant == 0:
        x = round((polynomial['1'] * -1) / (2 * polynomial['2']), 6)
        output += f"Discriminant is 0, the equation has only one solution:\n{str(x)}"
        make_details(details=details, polynomial=polynomial, x_1=x)
    else:
        output += "Discriminant is strictly negative, the equation has no solutions."
    return output, details


def square(number, i, j):
    mid = (i + j) / 2
    mul = mid * mid
    # If mid itself is the square root, return mid
    if (mul == number) or (abs(mul - number) < 0.00001):
        return mid
    # If mul is less than number, recur second half
    elif mul < number:
        return square(number, mid, j)
    # Else return first half
    else:
        return square(number, i, mid)


def find_square(number):
    i = 1
    # While the square root is not found
    find_root = False
    while find_root is False:
        # If number is a perfect square
        if i * i == number:
            return i
        elif i * i > number:
            # Square root will lie in the interval i-1 and i
            res = square(number, i - 1, i)
            return "{0:.5f}".format(res)
        i += 1
