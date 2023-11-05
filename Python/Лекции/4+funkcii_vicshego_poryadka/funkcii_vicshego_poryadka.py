import os

print(os.getcwd())
# def calc1(a, b):
#     return a + b
#
#
# def calc2(a, b):
#     return a * b
#
#
# def summ(op, x, y):
#     print(op(x, y))
#
#
# # summ(calc1, 5, 4)
# #
# # calc3 = lambda a, b: a + b
# # summ(calc3, 4, 5)
# #
# # summ(lambda a, b: a + b, 5, 4)
#
#
# # data = [1, 2, 3, 5, 8, 15, 23, 38]
# # out = []
# # for i in data:
# #     if i % 2 == 0:
# #         out.append((i, i ** 2))
# # print(out)
#
#
#
#

#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
#
#
# # list_1 = [x for x in range(1,20)]
# # print(list_1)
# #
# # list_1 = list(map(lambda x : x + 10, list_1))
# # print(list_1)
#
# data = "12 34 56 2  56 88 4 23 "
# print(data)
#
# data = list(map(int,data.split()))
# print(data)


# data = [15, 65, 9, 234, 175]
# res = list(filter(lambda x : x % 10 == 5, data ))
# print(res)
#
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)




# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)



# colors = ['red', '4434', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

#
    # with open("file.txt" , "w") as data:
    #     data.write("line 1\n")
    #     data.write("line 2\n")
    #
    # print(56)

path = "file.txt"
data = open("file.txt", "r")
for line in data :
    print(line)
data.close()

# print(os.path.basename("D:\GeekBrains\2.Python\Python\Лекции\4+funkcii_vicshego_poryadka"))
# print(os.path.abspath("funkcii_vicshego_poryadka.py"))