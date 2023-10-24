# # ОЁ
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
for i in range(0, len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
        print(i)

# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


# a1 = 5
# d = -1
# n = 10
# an = a1 + (n - 1) * d
# for i in range(a1, a1 + n  * d, d):
#     print(i)

# a1 = 2
# d = 3
# n = 4
# res_p = []
# def progress(a1, d, n):
#     if n == 0:
#         return ""
#     return progress(a1, d, n - 1) + str(a1 + (n-1) * d)
#
# print(f"{progress(2,3,4)}")

def func(min_number, max_number, i):
    if (i <= len(list_1)-1):
        if (max_number >= list_1[i] >= min_number):
            print(i)
            func(min_number, max_number, i+1)
        else:
            func(min_number, max_number, i+1)
    else:
        return
func(min_number, max_number, 0)


