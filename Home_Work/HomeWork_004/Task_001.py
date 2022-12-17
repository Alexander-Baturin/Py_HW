"""A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""
import random

size = int(input('Введите максимальную степень: '))
my_dict = {}
equation = ''

for i in range(size + 1):
    my_dict[i] = random.randint(0, size)
print(my_dict)

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
            elif i ==0:
                equation += f'{my_dict[i]} '
            else:
                equation += f'{my_dict[i]}*x**{i} + '
    if equation[:-1] == '':
        equation = equation[:-2]
print(equation + " = 0")

data = open('file_004001.txt', 'a')
data.writelines(equation + " = 0")
data.close()