# Задача 2. Напишимте программу для проверки истинности утверждения ¬X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите X - '))
y = int(input('Введите Y - '))
z = int(input('Введите Z - '))

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x | y | z) == (not x and not y and not z))
            print(x, y, z)
