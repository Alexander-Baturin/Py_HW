"""Функция поиска максимума"""
def MaxIntList(list):
    max = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
    return max

"""Функция поиска минимума"""
def MinIntList(list):
    min = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
    return min

"""Функция нахождения коэффициентов многочлена"""
def create_eq(size):
    my_dict = {}
    equation = ''

    for i in range(size + 1):
        my_dict[i] = random.randint(0, size)
    # print(my_dict)

    for i in range(size, -1, -1):
        if my_dict[i] != 0:
            if my_dict[i] == 1:
                if i == 1:
                    equation += f'x + '
                elif i == 0:
                    equation += f'1 '
                else:
                    equation += f'x**{i} + '
            else:
                if i == 1:
                    equation += f'{my_dict[i]}*x + '
                elif i == 0:
                    equation += f'{my_dict[i]} '
                else:
                    equation += f'{my_dict[i]}*x**{i} + '
            equation += f''
    if equation[:-1] == '':
        equation = equation[:-2]
    return equation + " = 0"