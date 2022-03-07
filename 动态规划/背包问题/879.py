from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        #背包问题：可以取多次；     ----先求出列坐标j较小的元素，故让循环变量j的值从小到大递增。
        #是0-1背包问题。只能取一次；----先求出列坐标j较大的元素，故让循环变量j的值从大到小递减。
        dp = [[0 for _ in range(minProfit + 1)] for _ in range(n + 1)]  #虚指
        
        for people in range(n + 1):
            dp[people][0] = 1           #前people个人，收益为0的方案有1种

        for cost, prof in zip(group, profit):       #遍历每份工作
            for people in range(n, cost - 1, -1):
                for money in range(minProfit, -1, -1):
                    dp[people][money] += dp[people - cost][max(0, money - prof)]
                    dp[people][money] %= 1000000007

        return dp[n][minProfit]



s = Solution()
s.profitableSchemes(n = 1, minProfit = 1, group = [1,2,1,1,2,2,1,1,1,1], profit = [0,0,0,0,1,1,1,1,2,2])
s.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8])

