nums = [1,4]
target = 4
l, r = 0, len(nums)
# 左闭右开
def search(l, r, way = None):
    while l < r:
        mid = (l+r)//2

        if nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            if way == 'left':
                return l if nums[l] == target else search(l+1, mid+1, way)
            elif way == 'right':
                return r-1 if nums[r-1] == target else search(mid, r-1, way)
            else:
                i = search(l, mid+1, way='left')
                j = search(mid, r, way='right')
                print(i, j)
                return [i, j]
    return [-1, -1]

print(search(l, r))