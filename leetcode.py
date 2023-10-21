# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
#
#
# def mergeTwoLists(self, list1, list2):
#     for j in list2:
#         list1.append(j)
#         list1 = sorted(list1)
#     print(list1)
# mergeTwoLists(list1, list2)

# 26. Удалить дубликаты из отсортированного массива
# nums = [1, 4, 8, 3, 5, 8, 53, 6, 9, 1,1,1,1]
#
#
# def removeDuplicates(nums):
#     j = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[j] = nums[i]
#             j += 1
#     return j
#
# print(removeDuplicates(nums))

