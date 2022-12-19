"""B. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов."""

import random

size_1 = int(input('Введите максимальную степень: '))
size_2 = int(input('Введите максимальную степень: '))

my_dict_1 = {}
my_dict_2 = {}

new_str_1 = []
new_str_2 = []

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
        else:
            if i == 0:
                equation = equation[:-3]
    return equation + " = 0"


my_str_1 = create_eq(size_1)
print(f'Первый многочлен: {my_str_1}')
my_str_1 = my_str_1.replace(' ', '')
# print(my_str_1)
my_str_1 = my_str_1[: -2].split('+')
# print(f'{my_str_1}\n')

for item in my_str_1:
    if item[0] == 'x':
        item = item.replace('x', '1')
        new_str_1.append(int(item[0]))
        new_str_1.append(int(item[-1]))
        continue
    elif item[-1] == 'x':
        item = item.replace('x', '1')
        new_str_1.append(int(item[0]))
        new_str_1.append(int(item[-1]))
    elif item[0] == 'x' and item[-1] == 'x':
        new_str_1.append(1)
        new_str_1.append(1)
    else:
        if len(item) > 1:
            new_str_1.append(int(item[0]))
            new_str_1.append(int(item[-1]))
        else:
            new_str_1.append(int(item[0]))
            new_str_1.append(0)
# print(new_str_1)

new_str_1.reverse()
my_dict_1 = {new_str_1[i]: new_str_1[i + 1] for i in range(0, len(new_str_1), 2)}
# print(my_dict_1)

my_str_2 = create_eq(size_2)
print(f'Второй многочлен: {my_str_2}')
my_str_2 = my_str_2.replace(' ', '')
# print(my_str_2)
my_str_2 = my_str_2[: -2].split('+')
# print(f'{my_str_2}\n')

for item in my_str_2:
    if item[0] == 'x':
        item = item.replace('x', '1')
        new_str_2.append(int(item[0]))
        new_str_2.append(int(item[-1]))
        continue
    elif item[-1] == 'x':
        item = item.replace('x', '1')
        new_str_2.append(int(item[0]))
        new_str_2.append(int(item[-1]))
    elif item[0] == 'x' and item[-1] == 'x':
        new_str_2.append(1)
        new_str_2.append(1)
    else:
        if len(item) > 1:
            new_str_2.append(int(item[0]))
            new_str_2.append(int(item[-1]))
        else:
            new_str_2.append(int(item[0]))
            new_str_2.append(0)
# print(new_str_2)
# for i in new_str_2:
#     print(i, type(i))
new_str_2.reverse()
my_dict_2 = {new_str_2[i]: new_str_2[i + 1] for i in range(0, len(new_str_2), 2)}

# print(my_dict_2)
my_dict_fin = {}

new_str = []
new_str.append(my_dict_1)
new_str.append(my_dict_2)
# print(new_str)

for dictionary in new_str:
    for key in dictionary:
        try:
            my_dict_fin[key] += dictionary[key]
        except KeyError:
            my_dict_fin[key] = dictionary[key]




# my_dict_1_keys, my_dict_2_keys = my_dict_1.keys(), my_dict_2.keys()
# key_list = set(my_dict_1_keys).union(set(my_dict_2_keys))
# print(f'key_list = {key_list}')
# print(type(key_list))

#     if i in my_dict_1:
#         if i in my_dict_1 == i in my_dict_2:
#             my_dict_fin[i] = my_dict_1[i] + my_dict_2[i]
#             print(f'my_dict_fin[{i}] = {my_dict_fin[i]}')
#             continue
#         else:
#             my_dict_fin[i] = my_dict_1[i]
#             print(f'my_dict_fin[{i}] = {my_dict_fin[i]}')
#     else:
#         my_dict_fin[i] = my_dict_2[i]
#         print(f'my_dict_fin[{i}] = {my_dict_fin[i]}')

# print(f'my_dict_fin = {my_dict_fin}')

max = 0
sum_size = max

for i in my_dict_fin:
    if i > max:
        max = i
    else:
        i += 1
sum_size = max
# print(f'sum_size = {sum_size}')

for i in my_dict_fin:
    i = str(i)
    # print(type(i))
    for j in i:
        j = str(j)
        # print(type(j))

equation_fin = ''

for i in reversed(my_dict_fin):
    if my_dict_fin[i] != 0:
        if my_dict_fin[i] == 1:
            if i == 1:
                equation_fin += f'x + '
            elif i == 0:
                equation_fin += f'1 '
            else:
                equation_fin += f'x**{i} + '
        else:
            if i == 1:
                equation_fin += f'{my_dict_fin[i]}*x + '
            elif i == 0:
                equation_fin += f'{my_dict_fin[i]} '
            else:
                equation_fin += f'{my_dict_fin[i]}*x**{i} + '
        equation_fin += f''
    else:
        if i == 0:
            equation_fin = equation_fin[:-3]

print(f"Сумма многочленов равна: {equation_fin} = 0")

data = open('file_004002.txt', 'w')
data.writelines(equation_fin + " = 0")
data.close()