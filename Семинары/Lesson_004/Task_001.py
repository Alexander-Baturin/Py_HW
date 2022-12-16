# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.


# my_list = []
#
# while True:
#     string = input('Введите числа через пробел: ')
#     for i in string:
#         if not i.isdigit():
#             break
#     else:
#         if string != '':
#             my_list.append(int(string))
#         else:
#             break

my_string = input('Введите числа через пробел: ')
#print(my_string)
my_string = my_string.strip().split(' ')
# strip правит ввод если там была синтакчическая ошибка (пробел вначале или в конце и т.д.)

my_list = []

for i in range(len(my_string)):
    my_list.append(my_string[i])
    my_list[i] = int(my_list[i])

# print(my_list)
max = my_list[0]
for i in range(len(my_list)):
    if max < my_list[i]:
        max = my_list[i]

print(max)