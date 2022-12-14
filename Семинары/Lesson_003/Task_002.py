# Задача 2. Напишите программу, которая определит позицию второго вхождения строки в списке (полное соответствие)
# либо сообщит, что ее нет.

my_list = ['qwe', 'asd', 'zxc', 'qwe', 'dfg', 'cvb']
search_string = input('Ведите символ: ')

count = 0
for i in range(len(my_list)):
    if my_list[i] == search_string:
        count += 1
    if count == 2:
        print(f'список - {my_list}, ищем :{search_string}, ответ: {i}')
        break
else:
    print(f'список - {my_list}, ищем :{search_string}, ответ: False')
