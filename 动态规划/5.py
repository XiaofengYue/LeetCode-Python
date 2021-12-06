class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [[False] * length for i in range(length)]
        cur_len = 0
        max_len = 1
        start = 0
        # 右闭 左 闭
        for right in range(1,length):
            for left in range(right):
                if right - left <= 2:
                    if s[left] == s[right]:
                        dp[left][right] = True
                        cur_len = right-left+1
                else:
                    if s[right] == s[left] and dp[left+1][right-1]:
                        dp[left][right] = True
                        cur_len = right-left+1
                if dp[left][right]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = left
        return s[start:start+max_len]

s = Solution()
s.longestPalindrome("babad")