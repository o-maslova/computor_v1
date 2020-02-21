def find_monomials_with_one_degree(polynomial: list):
    tmp_dict = {}
    i = 0
    while i < len(polynomial):
        polynomial[i].create_monomial()
        num_type = float if polynomial[i].is_float else int
        sign = polynomial[i].sign
        number = polynomial[i].number
        if polynomial[i].degree not in tmp_dict.keys():
            tmp_dict[polynomial[i].degree] = num_type(sign + number)
        else:
            tmp_dict[polynomial[i].degree] = tmp_dict[polynomial[i].degree] + num_type(sign + number)
            polynomial.pop(i)
            i -= 1
        i += 1
    return tmp_dict


def make_reduced_form(polynomial: list):
    tmp_dict = find_monomials_with_one_degree(polynomial)
    output = ""
    for elem in polynomial:
        elem.create_monomial()
        if elem.degree in tmp_dict.keys():
            new_num = str(tmp_dict.get(elem.degree))
            if new_num[0] == '-':
                elem.sign = '-'
                elem.number = new_num[1:]
            else:
                elem.number = new_num
        output += elem.__str__().upper() + " "
    output += "= 0"
    return output, tmp_dict
