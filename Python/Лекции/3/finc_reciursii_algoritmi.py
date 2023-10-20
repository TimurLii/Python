# def qick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greator = [i for i in array[1:] if i >= pivot]
#     return qick_sort(less) + [pivot] + qick_sort(greator)
#
#
# print(qick_sort([11, 12, 13, 16, 2, 3, 4, 5]))
#
#
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


arr = [3, 6, 8, 5, 3, 8, 0, 5, 2, 4, ]
merge_sort(arr)
print(arr)
