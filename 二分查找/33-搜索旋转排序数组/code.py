class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)
        def search(l, r):
            while r-l>1 and nums[l] == nums[l+1] :
                l = l+1
            while r-l>1 and nums[r-1] == nums[r-2]:
                r = r-1
            while l < r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                else:
                    if nums[l] <= nums[mid]: # 左边有序 
                        if nums[l] <= target and nums[mid] >= target:
                            # 目标在左边了
                            return search(l, mid)
                        else:
                            return search(mid+1, r)
                    else: # 右边有序
                        if nums[mid] <= target and nums[r-1] >= target:
                            # 目标在右边了
                            return search(mid+1, r)
                        else:
                            return search(l, mid)
            return False
        return search(l, r)