# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint as rnd
import random

size = int(input('Введите размер списка: '))
rnd_list = [random.randint(0, size) for i in range(size)]

for i in range(size):
    if size % 2 == 0:
        center = int(len(rnd_list) / 2)
    else:
        center = int(len(rnd_list) / 2 + 1)

new_list = []

for i in range(center):
    new_list.append(rnd_list[i] * rnd_list[len(rnd_list) - 1 - i])

print(f'{rnd_list} => {new_list}')
