# Задача 3. Реализуйте алгоритм перемешивания списка

from random import randint as rnd
import random

size = int(input('Введите размер списка: '))
rnd_list = []

for  i in range(size):
    rnd_list.append(rnd(0,10))

print(rnd_list)