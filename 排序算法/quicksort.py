
nums = [1,2,3,4,5,6]

# 作弊右闭
def quick_sort(left, right):
    if left >= right:
        return 

    mid_val = nums[left]
    low, high = left, right

    while low < high:
        while low<high and nums[high] >= mid_val:
            high -= 1
        nums[low] = nums[high]
        while low<high and nums[low] <= mid_val:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid_val

    quick_sort(left, low-1)
    quick_sort(low+1, right)

quick_sort(0, 5)