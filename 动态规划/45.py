class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now_index = 0
        jump = 0
        # 下标小于最后一个数字的下标时 应该进行跳跃操作
        while now_index < len(nums)-1:
            now_can_jump = nums[now_index]

            temp = 0
            temp_i = 0
            for i in range(now_index+1, now_index+1+now_can_jump):
                # 如果能跳出整个数组时、不必找最大一跳。直接跳出去
                if i >= len(nums)-1 :
                    return jump +1
                if nums[i] + i > temp:
                    temp = nums[i] + i
                    temp_i = i
            
            now_index = temp_i
            jump += 1
        return jump


s = Solution()
s.jump([2,3,1])