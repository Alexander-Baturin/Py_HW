# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('Введите число: '))

def Summa(num):
    if num < 0:
        num = num*(-1)

    number = 0

    for i in str(num):
        if i != '.':
            number += int(i)
    return(number)

print(f'{num} -> {Summa(num)}')