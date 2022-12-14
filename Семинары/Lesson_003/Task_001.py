# Задайте список. Напшите программу, которая определит, присутстует ли в заданном спимке строк некий символ.

my_list = ['skef646bhu4', 'nci4784cg', 'kahe64fgbf', 'kbh54']
symbol = input('Введите число: ')

# Первый вариант решения цикл в цикле:

# for item in my_list:# for item in range(len(my_list)) при такой постановке условия мы перебираем номера индекса
#     for char in item:# for char in my_list[item]
#         if char == symbol:
#             print(f'Символ {symbol} присутствует в строке {item}')
#             break# continue - после нахождения цифры запускает цикл на новую итерацию
#     else:
#         print(f'Символ {symbol} ОТСУТСТВУЕТ в строке {item}')

# Второй вариант решения задачи:

# for item in my_list:
#    if symbol in item:
#        print(f'Символ {symbol} присутствует в строке {item}')
#    else:
#        print(f'Символ {symbol} ОТСУТСТВУЕТ в строке {item}')
#    Такой вариант тоже допустим, в предыдущем мы рассматривали цикл в цикле

# Третий вариант решения с добавлением обоз начения позиции в принте:

for item in my_list:
    count = 0
    for i in range(len(item)):
        if symbol == item[i]:
            count +=1
            print(f'Символ {symbol} присутствует в строке {item}'
                  f'на {i} позиции')
    print(f'Символ {symbol} присутствует в строке {item}'
          f' {count} раз')
    # else:
    #     print(f'Символ {symbol} ОТСУТСТВУЕТ в строке {item}')

# Для замены элемента строки:

# print(my_list)
# for i in range(len(my_list)):
#     my_list[i] = my_list[i].replace(f'{symbol}', 'A')
# print(my_list)

# На вывод пойдет одна и та же информация:

# for item in my_list:
#     print(item)
# for i in range(len(my_list)):
#     print(my_list[i])

# print('\n') - выводит пустую строку

# Пример работы JOINа со списками:
# string = 'asdfgh'
# print(string)
# string = list(string)
# print(string)
#
# string = ''.join(string)# в кавычках может быть любой разделитель (-,  , ,., и т.д.)
# print(string)
# еще один вариант склеивания элементов списка в строку (в продолжение к предыдущему):
# new_string = []
# for i in range(0, len(string), 2):
#     #        от 0 до длины строки с шагом два
#     new_string.append(string[i] + string[i+1])
# print(new_string)

# так же без применения join можно сделать следующее:
# new_string = ''
# for i in string:
#     new_string += i
# print(new_string)
#    def my_join(list, separator):
#        new_string = ''
#        for i in list:
#             new_string += i + separator
#         return new_string[:-len(separator)]
#
#     print(my_join(string, '-'))