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

# com_set = itertools.permutations(rnd_list, size)# вариант подсмотренный в интернете
# for i in com_set:
#     print(i)

# k = -1
# for i in range(len(rnd_list)//2):
#     rnd_list[k], rnd_list[i] = rnd_list[i], rnd_list[k]
#     print(rnd_list)
#     k -= 1

for i in range(len(rnd_list)):# решение 1 после разбора дз на семенаре
    k = random.randint(0, (len(rnd_list) - 1))
    rnd_list[i], rnd_list[k] = rnd_list[k], rnd_list[i]
print(rnd_list)

for i in range(len(rnd_list)):# решение 2 после разбора дз на семенаре
    k = random.randint(0, (len(rnd_list) - 1))
    rnd_list.append(rnd_list.pop(k))
print(rnd_list)