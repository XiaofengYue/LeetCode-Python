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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        max_len=1
        index = 0
        for end in range(1, len(s)):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start < 2:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start+1][end-1]
                if dp[start][end]:
                    if end-start+1 > max_len:
                        max_len = end-start+1
                        index = start
        return s[index:index+max_len]

s = Solution()
s.longestPalindrome("babad")