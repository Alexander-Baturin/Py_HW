# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint as rnd
import random

size = int(input('Введите размер списка: '))
rnd_list = []

for i in range(size):
    rnd_list.append(rnd(0, size))

# print(rnd_list)
# print()


# new_list = []# мой вариант решения (не работает при списке более 5 элементов)
# k = -1
#
# for i in range(len(rnd_list)):
#     if i <= (len(rnd_list) % 2) + 1:
#         new_list.append(rnd_list[i] * rnd_list[k])
#         i += 1
#         k -= 1
#
# print(f'{rnd_list} => {new_list}')

if size % 2 == 0:
    center = int(len(rnd_list)/2)
else:
    center = int(len(rnd_list) / 2 + 1)

new_list = []

for i in range(center):
    new_list.append(rnd_list[i] * rnd_list[len(rnd_list) - 1 - i])

print(f'{rnd_list} => {new_list}')