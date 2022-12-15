# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

my_list = []
my_list.append(input('Введите первое значение списка: '))
my_list.append(input('Введите второе значение списка: '))
my_list.append(input('Введите тоетье значение списка: '))
my_list.append(input('Введите четвертое значение списка: '))
my_list.append(input('Введите пятое значение списка: '))

print('\n')
print(my_list)
print()

new_list = []
float_list = []
max = 0

for item in my_list:
    float_list.append(float(item))

# print(float_list)

for item in range(len(float_list)):
    new_list.append(float_list[item] % 1)

print(new_list)

for i in range(len(new_list)):
    if new_list[i] > max:
        max = i
        i += 1
    else:
        min = i
        i += 1

for i in  range(len(new_list)):
    min = 1
    if 0 < new_list[i] < min:
        min = i
        i += 1
    else:
        i += 1
print(f'max = {max}, min = {min}')

sub = round(max - min), 2


print(f'{my_list} => {sub}')