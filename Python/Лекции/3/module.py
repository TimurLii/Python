def max1(a, b):
    if a > b:
        return a
    return b


def sum_numbers(n, y="hello"):
    print(y)
    summa = 0
    for i in range(1, n ):
        summa += i
    return (summa)


def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 15):
    list_1.append(fib(i))
print(list_1)

