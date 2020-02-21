import sys
from app_logic.parsing import parser, define_degree, check_input
from app_logic.make_reduce_form import make_reduced_form
from app_logic.solving import solve_equation


def solving_process(polynomial_string):
    if not check_input(polynomial_string):
        print("It is not a polynomial equation!")
        raise SystemExit
    polynomial = parser(polynomial_string)
    if not polynomial:
        print("Wrong sequence of unknown parameters!")
        raise SystemExit
    degree = define_degree(polynomial)
    if int(degree) > 2:
        output = "The polynomial degree is strictly greater than 2, I can't solve."
    else:
        reduced, tmp = make_reduced_form(polynomial)
        solution = solve_equation(tmp)
        output = f"Reduced form: {reduced}\n"
        output += f"Polynomial degree: {degree}\n"
        output += solution
    print(output)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "--test":
        with open('tests.txt', 'r') as fd:
            test_string = fd.readline()
            while test_string:
                print(f"Test case: {test_string}")
                solving_process(test_string)
                test_string = fd.readline()
                print("\n\n")
    elif len(sys.argv) == 2:
        solving_process(sys.argv[1])
    else:
        print("Wrong input!")
