# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(10))

# ///////////////////////////////////////////////////////////


# def vasiliy(*nums):
#     res = []
#     for i in nums:
#         if i > 3:
#             i = 1
#             res.append(i)
#     print(res)
#
#
# vasiliy(5, 5, 5, 5, 5)
# //////////////////////////////////////////////////////////////


# def mass(*n):
#     print(n[::-1])
#
#
# mass(1,2,3,4,5,6,)


# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[::-1])

# ///////////////////////
# factorial

# def fact(n):
#     if n == 1:
#         return n
#     return n * fact(n - 1)
#
#
# print(fact(5))

# ????????????????????????????????
z = int(input("Введите число: "))
def nat(z, x = 2):
    if z == 2 or x * x > z:
        return True
    elif z % x == 0:
        return False
    return nat(z, x + 1)

print(nat(z))
