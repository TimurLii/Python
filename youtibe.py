# strs = ["flower", "flow", "flight"]
# ans = ""
# for i in strs:
#     for j in i:
#         if j == i:
#             ans += i
#
# print(ans)

# d = dict.fromkeys([1,2,3,4,5], "values")
# print(d)
d1 = dict([[6, 2], [8, 9]])
d2 = dict([[1, 2], [3, 4], [5, 6]])
# print(d2)
# print(d2[3])
#
# print(d2.items())
# print(d2.keys())
# print(d2.values())
# d1.update(d2)
# print(d1)

t = d1.pop(6)
print(t, d1)
