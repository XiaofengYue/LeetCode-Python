class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归方式
        if n == 1:
            return 1
        if n & 1 == 0:
            return 1 + self.integerReplacement(n//2)
        return 2 + min(self.integerReplacement((n+1)//2), self.integerReplacement((n-1)//2))

s = Solution()
s.integerReplacement()


