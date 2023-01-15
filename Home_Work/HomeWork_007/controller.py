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

def str_expression(expression: list):
    result = 0
    if '(' in expression:
        result = check_parentheses(expression)
        result = string_calc(result)
    else:
        result = string_calc(expression)
    model.set_result(result)
def string_calc(expression: list):
    # expression = expression.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
    #     replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
    new_expression = []
    for item in expression:
        if isinstance(item, int):
            new_expression.append(int(item))
        else:
            new_expression.append(item)
    while len(new_expression) > 1:
        i = 0
        while (('*' in new_expression) or ('/' in new_expression)) and i < len(new_expression):
            if new_expression[i] == '*':
                result = int(new_expression[i-1]) * int(new_expression[i+1])
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            elif new_expression[i] == '/':
                result = int(new_expression[i-1]) / int(new_expression[i+1])
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
        while (('+' in new_expression) or ('-' in new_expression)) and i < len(new_expression):
            if new_expression[i] == '+':
                result = int(new_expression[i-1]) + int(new_expression[i+1])
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            elif new_expression[i] == '-':
                result = int(new_expression[i-1]) - int(new_expression[i+1])
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
    return new_expression[0]
    # print(new_expression[0])

def check_parentheses(expression):
    while '(' in expression:
        open_index, close_index = 0, 0
        for i in range(len(expression)):
            if expression[i] == '(':
                open_index = i
            if expression[i] == ')':
                close_index = i
                break
        else:
            return expression
        first_expr = expression[0:open_index]
        part_expr = expression[open_index+1:close_index]
        last_expr = expression[close_index+1:]
        expression = first_expr + [string_calc(part_expr)] + last_expr
    return expression

def valid_expression(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.insert(0, char)
        if char == ')':
            if len(stack) > 0:
                stack.pop(0)
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True
def first_input():
    while True:
        number = view.first_input()
        number = number.strip().replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * '). \
            replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        if number[0] == '-':
            number[0] = int(number[0] + number[1])
            number.pop(1)
        if len(number) < 2:
        #     model.set_first(number)
            while True:
                input_operation()
                if model.get_operation() == '=':
                    view.log_of()
                    break
                input_second()
                solution()
        else:
            if valid_expression(number):
                str_expression(number)
            else:
                print('Введено некорректное выражение')
        result = model.get_result()
        view.print_result(result)
        retry = input('Посчитать еще одно выражение? (y/n)')
        if retry == 'n':
            break


# def start():
#     input_first()
#     while True:
#         input_operation()
#         if model.get_operation() == '=':
#             view.log_of()
#             break
#         input_second()
#         solution()