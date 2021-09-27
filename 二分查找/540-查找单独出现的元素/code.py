
def findSingleNumber():
    pass

nums = [3,3,7,7,10,11,11]

l, r = 0, len(nums) #left close right open

if r == 1:
    # return nums[0]
    pass

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
            # return nums[mid]
            print(nums[mid])
    else: # mid is not odd
        if mid+1<len(nums) and nums[mid] == nums[mid+1]:
            l = mid + 1
        elif mid != 0 and nums[mid] == nums[mid -1]:
            r = mid
        else:
            # return nums[mid]
            print(nums[mid])
            


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
