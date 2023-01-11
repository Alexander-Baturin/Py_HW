import view
import model

def input_first():
    number = view.input_number()
    model.set_first(number)

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break


def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
    else:
        return True
    # result = model.get_result()
    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def string_calc(expression: str):
    expression = expression.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
        replace('/', ' / ').split()
    new_expression = []
    for item in expression:
        if item.isdigit():
            new_expression.append(int(item))
        else:
            new_expression.append(item)
    while len(new_expression) > 1:
        i = 0
        while (('*' in new_expression) or ('/' in new_expression)) and i < len(new_expression):
            if new_expression[i] == '*':
                result = new_expression[i-1] * new_expression[i+1]
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            elif new_expression[i] == '/':
                result = new_expression[i-1] / new_expression[i+1]
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
        while (('+' in new_expression) or ('-' in new_expression)) and i < len(new_expression):
            if new_expression[i] == '+':
                result = new_expression[i-1] + new_expression[i+1]
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            elif new_expression[i] == '-':
                result = new_expression[i-1] - new_expression[i+1]
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
    print(new_expression[0])


def first_input():
    number = view.first_input()
    if number.isdigit():
        model.set_first(number)
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_of()
                break
            input_second()
            solution()
    else:
        string_calc(number)


# def start():
#     input_first()
#     while True:
#         input_operation()
#         if model.get_operation() == '=':
#             view.log_of()
#             break
#         input_second()
#         solution()