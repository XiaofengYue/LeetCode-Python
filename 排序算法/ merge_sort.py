
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    res = []
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res

print(merge_sort([1,6,2,5,7]))