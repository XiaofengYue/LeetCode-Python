class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) == 1: return 1
 
        legalstr = set(str(i) for i in range(1, 27))
 
        dp = [0] * (len(s))
        dp[0] = 1 
        if s[1] not in legalstr:  # s[1]为0
            dp[1] = 1 if s[ : 2] in legalstr else 0
        else:
             dp[1] = 2 if s[ : 2] in legalstr else 1            
 
        # 因为要用到i-2 所以至少初始化 dp[0] dp[1]
        for i in range(2, len(s)):
            if s[i] not in legalstr:
                if s[i - 1: i + 1] not in legalstr:
                    return 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if s[i - 1: i + 1] in legalstr:
                    dp[i] = dp[i - 1]+dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]

作者：sheldonxin
链接：https://leetcode-cn.com/problems/decode-ways/solution/chao-xiang-xi-cong-bao-li-di-gui-dao-don-6vwr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。