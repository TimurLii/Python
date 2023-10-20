# coins = [0, 1, 0, 1, 1, 0,1,0,0,0]
#
# count0 = 0
# count1 = 0
# for i in coins:
#     if i ==1:
#         count1 = count1 +1
#     if i ==0:
#         count0= count0 +1
# if count1> count0:
#     print(count0)
# else :
#     print (count1)
# //////////////////////////////////////////////////////////
# n = 3
# sum = 0
# while 2**sum <= n:
#     print(2**sum)
#     sum+=1
# ///////////////////////////////////////////////////////////
# x = 12
# y = 27
# s = 0
# p = 0
#
# for i in range(1000):
#     for j in range(1000):
#         if i + j == x and i * j == y:
#             print (i,j)
# /////////////////////////////////////////////////////////////////

ves = [5, 1, 5, 6, 9]
maxi = 0
mini = 1
for i in ves:
    if i <= mini:
        mini = i
    if i >= maxi:
        maxi = i
print(mini, maxi)
