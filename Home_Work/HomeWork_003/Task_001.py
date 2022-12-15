# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с
# нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd
import random

size = int(input('Введите размер списка: '))
rnd_list = []

for i in range(size):
    rnd_list.append(rnd(0, size))

# print(rnd_list)
summa = 0
count = 0

for i in range(len(rnd_list)):
    if count % 2 !=0:
        # print(rnd_list[i])
        count += 1
        summa += rnd_list[i]

    else:
        count+=1


print(f'{rnd_list} -> сумма нечетных элементов - {summa}')