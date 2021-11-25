# https://blog.csdn.net/believexfr/article/details/52823883
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        pig_entropy = minutesToTest//minutesToDie + 1
        i = 1
        while True:
            if pow(pig_entropy, i) >= buckets:
                return i
            i+=1

# 好题当赏
s = Solution()
s.poorPigs(1, 1, 1)