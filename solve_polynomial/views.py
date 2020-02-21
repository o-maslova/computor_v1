from django.shortcuts import render
from .forms import InputForm
from app_logic.parsing import parser, define_degree
from app_logic.make_reduce_form import make_reduced_form
from app_logic.solving import solve_equation


def make_beautiful_solution(solution: str):
    i = 0
    output = ""
    solution = solution.replace('\n', '<br>')
    # output = solution
    tmp = solution.find(':', i)
    while tmp != -1:
        print(tmp)
        end = tmp + 1 + len('<br>')
        output += "<b>" + solution[i:end] + "</b>"
        tmp_2 = solution.find('<br>', tmp)
        i += tmp_2 + len('<br>')
        output += solution[end:i]
        tmp = solution.find(':', i)
        # output += solution[tmp_2:tmp]
        print(output)
    return output


def index(request):

    form = InputForm()
    content = {
        'form': form,
        'reduced': '',
        'degree': '',
        'solution': '',
        'error': ''
    }
    if request.method == "POST":
        form = InputForm(request.POST)
        content['form'] = form
        if form.is_valid():
            polynomial_string = form.cleaned_data['input']
            polynomial = parser(polynomial_string)
            if not polynomial:
                content['error'] = "Wrong sequence of unknown parameters!"
                return render(request, 'index.html', content)
            tmp = define_degree(polynomial)
            if int(tmp) > 2:
                content['error'] = "The polynomial degree is strictly greater than 2, I can't solve."
            else:
                content['degree'] = tmp
                content['reduced'], tmp = make_reduced_form(polynomial)
                output, details = solve_equation(tmp)
                content['solution'] = make_beautiful_solution(output)
                content['details'] = make_beautiful_solution(details)
    return render(request, 'index.html', content)
