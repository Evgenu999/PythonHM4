# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число "))
simple_multipliers = []

while n >= 2:
    if not n % 2:
        simple_multipliers.append(2)
        n /= 2
    elif not n % 3:
        simple_multipliers.append(3)
        n /= 3
    elif not n % 5:
        simple_multipliers.append(5)
        n /= 5
    elif not n % 7:
        simple_multipliers.append(7)
        n /= 7

print(simple_multipliers, end=' ')