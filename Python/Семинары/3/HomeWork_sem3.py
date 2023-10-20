# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
# k = 13
# sort = sorted(list1)
# for i in sort:
#     if i == k:
#         print(sort[k:i+1])


# //////////////////////////////////////////////////////////
# k = 'laptopq'
# dictionary = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ ": 2, "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5, "JXШЭЮ": 8,
#               "QZФЩЪ": 10}
# k = k.upper()
# sum = 0
# for j in k:
#     for i in dictionary:
#         if j in i:
#             sum +=dictionary[i]
# print(sum)
# ???????????????????????????????????????????
# list1 = [1, 1, 2, 0, -1, 3, 4, 4, 5, 6]
# # первый способ
# out =[]
# count = 0
# for i in list1:
#     if i not in out:
#         out.append(i)
#         count += 1
# print(count)
# второй способ
# print(len(set(list1)))
