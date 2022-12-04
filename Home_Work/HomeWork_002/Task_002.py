# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

N = int(input('Введите количество чисел в списке: '))
my_list = []

for i in range(1, N+1):
    k = round((1+(1/i))**i,2)
    my_list.append(f'{k}')

print(my_list)

# def str_to_num(my_list):
#     str = str.strip()
#     if '.' in str and str.replace('.', '').isdigit():
#         return float(str)
#     elif str.isdigit():
#         return int(str)

# num_list = []
# for i in my_list:
#     n = str_to_num(i)
#     if n is not None:
#         num_list.append(str_to_num(i))
#
# print(num_list)
#
# sum(num_list)
# sum(my_list)
# print({sum()})
