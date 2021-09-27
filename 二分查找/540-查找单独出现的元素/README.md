## 思路
二分法！
很明显：单个元素的左边 (偶奇相等)，单个元素的右边（奇偶相等）
最关键的就是：一定要控制好边界是否越界！！！循环是否可以结束
## Code
```Python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) #left close right open
        if r == 1:
            return nums[0]
        
        while l < r:
            mid = (l+r)//2
            # judge odd 
            if mid%2==1: # mid is odd
                if nums[mid] == nums[mid-1]:
                    # left is ok , search right now
                    l = mid+1
                elif mid+1<len(nums) and nums[mid] == nums[mid+1]:
                    # right is ok , search left now
                    r = mid
                else:
                    return nums[mid]
                    # print(nums[mid])
            else: # mid is not odd
                if mid+1<len(nums) and nums[mid] == nums[mid+1]:
                    l = mid + 1
                elif mid != 0 and nums[mid] == nums[mid -1]:
                    r = mid
                else:
                    return nums[mid]
                    # print(nums[mid])
```