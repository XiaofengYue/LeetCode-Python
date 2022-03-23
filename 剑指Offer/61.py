from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()

        pre = -1
        flag = 0
        i = 0
        while i < 5:
            if nums[i] == 0:
                flag += 1
                i += 1
            else:
                if pre != -1:# 有前驱
                    if nums[i] != pre + 1: # 但是没法顺子
                        if flag > 0 :
                            flag -= 1
                            pre += 1
                        else:
                            return False
                    else:
                        pre += 1
                        i += 1
                else:
                    pre = nums[i]
                    i += 1
        return True

s = Solution()
s.isStraight([0,0,2,2,5])