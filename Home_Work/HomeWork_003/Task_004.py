# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите число: '))

# my_list = []
# while n > 0:
#     if n % 2 != 0:
#         my_list.insert(0, 1)
#         n = n//2
#
#     else:
#         my_list.insert(0, 0)
#         n = n // 2
#
# s = ''.join(map(str,my_list))
#
# print(f"{n} -> {s}")

bi_num = ''# вариант решения после разбора дз
while n > 0:
    bi_num = str(n % 2) + bi_num
    n //= 2
print(bi_num)