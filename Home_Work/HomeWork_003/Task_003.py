# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
import random

# my_list = []
# my_list.append(input('Введите первое значение списка: '))
# my_list.append(input('Введите второе значение списка: '))
# my_list.append(input('Введите тоетье значение списка: '))
# my_list.append(input('Введите четвертое значение списка: '))
# my_list.append(input('Введите пятое значение списка: '))
#
# print()
# print(my_list)
# print()
#
# new_list = []
# float_list = []
# max = 0
#
# for item in my_list:
#     float_list.append(float(item))
#
# # print(float_list)
#
# for item in range(len(float_list)):
#     new_list.append(float_list[item] % 1)
#
# print(new_list)
#
# for i in range(len(new_list)):
#     if new_list[i] > max:
#         max = i
#         i += 1
#     else:
#         min = i
#         i += 1
#
# for i in  range(len(new_list)):
#     min = 1
#     if 0 < new_list[i] < min:
#         min = i
#         i += 1
#     else:
#         i += 1
# print(f'max = {max}, min = {min}')
#
# sub = round(max - min), 2
#
#
# print(f'{my_list} => {sub}')

size = int(input('Введите размер списка: '))
my_list = [round(random.randint(0, 1000)) for _ in range(size)]
devine_list = [10, 100, 1000, 10000]

for i in range(len(my_list)):
    my_list[i] = my_list[i] / random.choice(devine_list)
print(my_list)

devine = list(map(lambda x: x - int(x), my_list))
devine = list(map(lambda x: round(x, 3), devine))

print(max(devine) - min(devine))