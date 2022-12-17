# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

N = int(input('Введите количество чисел в списке: '))
my_list = []

for i in range(1, N+1):
    k = round((1+(1/i))**i,2)
    my_list.append(f'{k}')

# print(my_list)
# print()

#print(sum(my_list,1))
def my_list_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)

num_list = []
for i in my_list:
    n = my_list_to_num(i)
    if n is not None:
        num_list.append(my_list_to_num(i))

print(num_list)
print()
#sum(num_list,1)
print(sum(num_list,1))
