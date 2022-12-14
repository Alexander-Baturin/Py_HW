# Задача 3. Напишите программу в которой пользователь будет задавть две строки, а программа будет определять
# количество вхождений одной строки в другую.

text = 'Первое число -1, второе число - 2, сумма - 3'
sub_text = input('Введите подстроку: ')

#print(text.count(sub_text)) - встроенный метод PyCharm

# Решение через "срезы":

#print(text[a:b:c])
#a - начальный индекс среза, b - финальный индекс среза, c - шаг

count = 0
for i in range(len(text)):
    if text[i:i+len(sub_text)] == sub_text:
        count += 1
print(f'Подстрока {sub_text} встречается в заданном тексте {count} раз')

# Как перевернуть строку:
# string = 'asdfg'
# print(string[::-1])

# insert строки:
# my_list =[0]
#
# for iu in range(1, 5):
#     my_list.append(5)
#     my_list.insert(0, -i)
#     print(my_list)
# print(my_list)