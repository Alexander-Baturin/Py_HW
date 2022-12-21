'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

path = r'E:\GeekBrains\Знакомство с Python\Home_Work\HomeWork_005\initdata_005001.txt'
my_str = ''

with open(path, 'r', encoding='UTF-8') as data:
   my_str = data.readline()

new_str = ''
prev_char =''
count = 1

for char in my_str:
    if char != prev_char:
        if prev_char:
            new_str += str(count) + prev_char
        count = 1
        prev_char = char
    else:
        count += 1
else:
    new_str += str(count) + prev_char

print(f'{my_str} => {new_str}')

dec_str = ''
count_str = ''

for char in new_str:
    if char.isdigit():
        count_str += char
    else:
        dec_str += char * int(count_str)
        count_str = ''

print(f'{new_str} => {dec_str}')

data = open('result_005001.txt', 'w')
data.writelines(my_str + ' => ' + new_str + ' => ' + dec_str)
data.close()