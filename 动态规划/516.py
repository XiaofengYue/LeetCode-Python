class Solution(object):
    def longestPalindromeSubseq(self, s):
        len_s = len(s)
        dp = [[0] * len_s for _ in range(len_s)]
        # base case 每个字符可以是一个回文串
        for i in range(len_s):
            dp[i][i]=1
        for i in range(len_s-1,-1,-1):
            for j in range(i+1,len_s):
                #长度加2
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]

class Solution(object):
    def longestPalindromeSubseq(self, s):
        dp = [[1]*len(s) for i in range(len(s))]
        for j in range(1, len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


s = Solution()
s.longestPalindromeSubseq('cbbdbcb')