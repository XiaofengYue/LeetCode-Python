from typing import List

class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [0] * (len(num) + 1)
        dp[1] = 1
        for i in range(1, len(num)): # i以num为参照下标
            dp[i+1] += dp[i]
            if num[i-1]!='0' and int(num[i-1:i+1]) <= 25:
                dp[i+1] += dp[i-1]
        
        return dp[-1]