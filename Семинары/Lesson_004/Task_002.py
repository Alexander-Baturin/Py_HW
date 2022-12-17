"""29. Задайте два числа. напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел"""

nums = input('Введите два числа через пробел: ')
nums = nums.strip().split(' ')
max_num = 0

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if max_num < nums[i]:
        max_num = nums[i]

# print(max_num)

for i in range(max_num, nums[0] * nums[1] + 1):
    if i % nums[0] == 0 and i % nums[1] == 0:
        print(i)
        break