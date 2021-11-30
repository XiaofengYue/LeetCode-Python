class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        while n > a*9*b:
            n -= a*9*b
            a += 1
            b *= 10
        n -= 1
        num = n//a + 10**(a-1)
        return str(num)[n%a]