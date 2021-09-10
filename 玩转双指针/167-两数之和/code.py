class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ### Version 1 ###
        # for i in range(len(numbers)):
        #     obj = target - numbers[i] # 需要找到的数字
        #     if obj in numbers[i+1:]:
        #         j = numbers.index(obj, i+1)
        #         return [i+1,j+1]

        ### Version 2 ###
        # i一直向右边前进 j根据两数之和来回前进
        # i, j = 0, 1
        # way = 1
        # while True:
        #     if numbers[i] + numbers[j] == target:
        #         return [i+1,j+1]
        #     else:
        #         # 一直向右前进 直到碰壁或者之和大于target
        #         if way == 1 and (j == len(numbers)-1 or numbers[i]+numbers[j] > target):
        #             way = -way
        #             i += 1
        #         # 一直向左前进 直到碰壁(i)或者之和小于Target
        #         elif way == -1 and (j == i+1 or numbers[i] + numbers[j] < target):
        #             way = -way
        #         else:
        #             j+= way
            
        ### Version 3 ###
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


s = Solution()
s.twoSum([3,24,50,79,88,150,345], 200)