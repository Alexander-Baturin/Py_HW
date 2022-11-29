# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8, 9 -> нет

print ('Введите первое число: ')
num_1 = int(input())

print ('Введите второе число: ')
num_2 = int(input())

pow_num_1 = num_1**2
pow_num_2 = num_2**2

if pow_num_1 == num_2:
    print(f'{num_1}, {num_2} -> да')
elif pow_num_2 == num_1:
    print(f'{num_2}, {num_1} -> да')
elif pow_num_1 != num_2:
    print(f'{num_1}, {num_2} -> нет')
elif pow_num_2 != num_1:
    print(f'{num_2}, {num_1} -> нет')