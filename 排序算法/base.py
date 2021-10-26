## 快速排序

# 左闭右开
nums = [6,5,3,1,8,7,2,4]
def quick_sort(l, r):
    if r - l <= 1 :
        return 
    # 闭区间的left 和 right
    temp, left, right = nums[l], l, r-1
    while left < right: # 尚且有元素可以遍历
        while left < right and nums[right] >= temp: # 写等于能节省时间复杂度
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= temp:
            left += 1
        nums[right] = nums[left]
    nums[left] = temp
    quick_sort(l, left)
    quick_sort(left+1, r) 

# quick_sort(0, len(nums))


## 归并排序

temp = [0] * len(nums)
def merge_sort(l, r):
    # 1.结束条件
    if r - l <= 1: 
        return
    mid = (r+l)//2
    # 2.分开
    merge_sort(l, mid)
    merge_sort(mid, r)
    # 3.合治
    index, l_index, r_index = l, l, mid
    while l_index<mid and r_index<r:
        if nums[r_index] < nums[l_index]:
            temp[index] = nums[r_index]
            r_index += 1
            index += 1
        else:
            temp[index] = nums[l_index]
            l_index += 1
            index += 1
    temp[index:index+mid-l_index] = nums[l_index:mid]
    temp[index:index+r-r_index] = nums[r_index:r]
    # 结果返回到nums中
    for i in range(l, r):
        nums[i] = temp[i]

merge_sort(0, len(nums))


# 插入排序
def insert_sort(n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp

# 冒泡排序
def bubble_sort(n):
    for i in range(1, n):# 控制循环次数
        for j in range(1, n-i+1):# 长度递减，最大值在最后
            if nums[j] < nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp

# 堆排序
def shift_down(arr, root, k):
    val = arr[root]
    while root<<1 < k:
        child = root << 1
        if child|1 < k and arr[child|1][1] < arr[child][1]: # 有右孩子并且右孩子小于左孩子
            child |= 1 # 孩子变为右孩子
        if arr[child][1] < val[1]:
            arr[root] = arr[child]
            root = child
        else:
            break
    arr[root] = val

def shift_up(arr, child):
    val = arr[child]
    while child>>1 >0 and val[1] < arr[child>>1][1]:
        arr[child] = arr[child>>1]
        child >>= 1
    arr[child] = val