from django.shortcuts import render
from .forms import InputForm
from app_logic.parsing import parser, define_degree
from app_logic.make_reduce_form import make_reduced_form
from app_logic.solving import solve_equation

def content_dict(form=''):
    return {
        'form': form,
        'reduced': '',
        'degree': '',
        'solution': '',
        'error': ''
    }


def make_beautiful_details(details: list):
    new_lst = []
    for elem in details:
        new_lst.append(elem.replace("\n", "<br>"))
    print(new_lst)
    return new_lst


def make_beautiful_solution(solution: str):
    i = 0
    output = ""
    solution = solution.replace('\n', '<br>')
    tmp = solution.find(':', i)
    output += "<b>" + solution[:tmp + 1] + "</b>"
    output += solution[tmp + 1:]
    return output


def index(request):

    form = InputForm()
    content = content_dict(form=form)

    if request.method == "POST":
        form = InputForm(request.POST)
        content['form'] = form
        if form.is_valid():
            polynomial_string = form.cleaned_data['input']
            polynomial = parser(polynomial_string)
            if not polynomial:
                content['error'] = "Wrong input!"
                return render(request, 'index.html', content)
            tmp = define_degree(polynomial)
            if int(tmp) > 2:
                content['error'] = "The polynomial degree is strictly greater than 2, I can't solve."
            else:
                content['degree'] = tmp
                content['reduced'], tmp = make_reduced_form(polynomial)
                output, details = solve_equation(tmp)
                content['solution'] = make_beautiful_solution(output)
                content['details'] = make_beautiful_details(details) if details else ''
    return render(request, 'index.html', content)
