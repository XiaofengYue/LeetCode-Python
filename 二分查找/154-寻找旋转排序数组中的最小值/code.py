
nums = [3,1]
l, r = 0, len(nums)

def search(l, r):
    res = nums[0]
    while l<r:
        if r - l == 2:
            res = min(res, nums[l])
            res = min(res, nums[r-1])
        # 重复数字需要缩小区间 左边重复
        while l<len(nums)-1 and nums[l] == nums[l+1]:
            l = l+1
        # 右边重复
        while r-1 > l and nums[r-1] == nums[r-2]:
            r = r-1
        mid = (l+r)//2
        if nums[mid] > nums[l]:
            res = min(res, nums[l])
            l = mid+1
        elif nums[mid] < nums[r-1]:
            res = min(res, nums[mid])
            r = mid
        else:
            l += 1
    return res

print(search(l, r))
