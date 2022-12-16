# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число N: '))

fib_1 = 1
fib_2 = 1
nfib_1 = 1
nfib_2 = -1
k = n
i = 0

my_list = []
my_list_fib = []
my_list_nfib = []
my_end_list = []

for item in range(n-1):
    my_list.append(item)
# print(my_list)
print()

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in my_list:
    fibonacci(n)
    my_list_fib.append(fibonacci(n))
    n -= 1
    i += 1

my_list_fib.append(fib_2)
my_list_fib.append(0)

# print(my_list_fib)
my_list_fib.reverse()
# print(my_list_fib)

# my_list.reverse()
# print(my_list)
# print()

# def nfibonacci(n):
#     if n in (1, 2):
#         return 1
#     return nfibonacci(n + 2) - nfibonacci(n + 1)

# for i in my_list:
#     nfibonacci(n)
#     my_list_nfib.append(nfibonacci(n))
#     n += 1
#     # i -= 1
# print(my_list_nfib)

my_end_list = my_list_nfib + my_list_fib

print(f'Для N = {k} список будет выглядеть так: {my_end_list}')