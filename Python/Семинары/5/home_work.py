# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

def stepen(a, b):
    if b <= 1:
        return a
    return a * stepen(a, b - 1)


print(stepen(3, 5))


# ////////////////////////////////////////
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# Функция не должна ничего выводить, только возвращать значение.
# sum(2, 2)
# # 4
def sum(a, b):
    if b < 1:
        return a
    return sum(a + 1, b - 1)


print(sum(8, 0))
