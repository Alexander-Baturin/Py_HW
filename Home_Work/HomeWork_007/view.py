


def first_input():
    first_input = input('Введите число или строчное выражение :')
    return first_input

def input_number() -> int:
    while True:
        try:
            number = int(input('Введите целое число: '))
            return number
        except:
            print('Ошибка')

def input_operation ():
    while True:
        operation = input('Введите математический оператор: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректный оператор')

def print_to_console(value_text):
    print(value_text)

def log_of():
    print('До новых встреч!')

def print_division_by_zero():
    print('На ноль делить нельзя!')

def print_result(value):
    print(f'Результат: {int(value)}')