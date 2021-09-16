# 思路
很明显就是二分查找、但是找左边和右边情况不一样，我们可以用递归+一个变量来控制递归方向

# 代码
```Python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

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
                        # print(i, j)
                        return [i, j]
            return [-1, -1]
        return search(l, r)

```