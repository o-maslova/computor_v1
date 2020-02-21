def solve_equation(polynomial: dict):
    """ 
        Discriminant formula: b^2 - 4 * a * c
        :param polynomial: dictionary which contain polynomial
        :return: 
    """
    if '2' in polynomial.keys() and polynomial.get('2') != 0:
        discriminant = polynomial['1'] ** 2 - 4 * polynomial['2'] * polynomial['0']
        output, details = discriminant_solutions(polynomial, discriminant)
        return output, details
    elif '0' in polynomial.keys() and '1' in polynomial.keys():
        res = polynomial['0'] * -1 / polynomial['1']
        return f"The solution is:\n{str(round(res, 6))}"
    elif ('0' in polynomial.keys() and polynomial['0'] == 0) or \
            ('1' in polynomial.keys() and polynomial['1'] == 0):
        return "All the real numbers are solution."
    elif '0' in polynomial.keys() and polynomial['0'] != 0 or \
            ('1' in polynomial.keys() and polynomial['1'] != 0):
        return "There is no solution."


def discriminant_solutions(polynomial: dict, discriminant: float):
    output = ""
    details = f"Discriminant = {str(discriminant)}\n"
    if discriminant > 0:
        output += "Discriminant is strictly positive, the two solutions are:\n"
        square_of_d = float(find_square(discriminant))
        x_1 = (polynomial['1'] * -1 - square_of_d) / (2 * polynomial['2'])
        x_2 = (polynomial['1'] * -1 + square_of_d) / (2 * polynomial['2'])
        output += f"{str(round(x_1, 6))}\n"
        output += f"{str(round(x_2, 6))}\n"
        details += f"Square root of discriminant: {square_of_d}\n" \
                   f"The first root is calculated by the formula: (-b - sqrt(D)) / 2a\n" \
                   f"First solution: ({str((polynomial['1'] * -1))}-{str(square_of_d)}) / 2 * {str(polynomial['2'])}\n" \
                   f"Result: {x_1}\n\n"
        details += f"The second root is calculated by the formula: (-b + sqrt(D)) / 2a\n" \
                   f"Second solution: ({str((polynomial['1'] * -1))}+{str(square_of_d)}) / 2 * {str(polynomial['2'])}\n" \
                   f"Result: {x_2}\n\n"
    elif discriminant == 0:
        x = (polynomial['1'] * -1) / (2 * polynomial['2'])
        output += f"Discriminant is 0, the equation has only one solution:\n{str(round(x, 6))}"
        details += f"The solution is found by the formula -b / 2a\n" \
                   f"Solution: {str((polynomial['1'] * -1))} / 2 * {str(polynomial['2'])}\n" \
                   f"Result: {x}"
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
