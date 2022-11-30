# Задача 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quart = int(input('Введите номер четверти - '))

if quart == 1:
    print(f'X = 1..+oo; Y = 1..+oo')
elif quart == 2:
    print(f'X = -1..-oo; Y = 1..+oo')
elif quart == 3:
    print(f'X = -1..-oo; Y = -1..-oo')
elif quart == 4:
    print(f'X = 1..+oo; Y = -1..-oo')
elif quart > 4:
    print('Отдохни и попробуй еще раз')