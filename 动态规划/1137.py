class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 2:
            x1, x2, x3 = 0, 1, 1
            for i in range(n-2):
                x3, x2, x1 = x1+x2+x3, x3, x2
            return x3
        return 0 if n == 0 else 1 