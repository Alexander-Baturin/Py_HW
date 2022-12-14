# Задача 2. Напишите программу, которая определит позицию второго вхождения строки в списке (полное соответствие)
# либо сообщит, что ее нет.

my_list = ['qwe', 'asd', 'zxc', 'qwe', 'dfg', 'cvb']
search_string = input('Ведите символ: ')

count = None
for item in my_list:
    for i in range(len(my_list)):
        if search_string == item[i]:
            count += i
        if count == 2:
            print(f'список - {my_list}, ищем :{search_string}, ответ: {i}')