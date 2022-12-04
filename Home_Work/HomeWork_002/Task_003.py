# Задача 3. Реализуйте алгоритм перемешивания списка
import itertools
from random import randint as rnd
import random

size = int(input('Введите размер списка: '))
rnd_list = []

for i in range(size):
    rnd_list.append(rnd(0,size))

print(rnd_list)
print()

# com_set = itertools.permutations(rnd_list, size)
# for i in com_set:
#     print(i)

# k = -1
# for i in range(len(rnd_list)//2):
#     rnd_list[k], rnd_list[i] = rnd_list[i], rnd_list[k]
#     print(rnd_list)
#     k -= 1