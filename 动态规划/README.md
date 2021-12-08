# DP问题 状态+天数+区分动作

**<u>*状态一个维度、天数一个维度、不能区分的动作一个维度*</u>**

***<u>只求最大值、不求具体解</u>***

## ==只买一次(买一次卖一次获得最大利润)==

`状态`：持有、不持有。（天数用一维、状态用一维）

`动作`：什么也不做、买、卖

DP 含义：拥有的价值

<img src="http://catbed.oss-cn-chengdu.aliyuncs.com/img/Screen%20Shot%202021-12-08%20at%204.05.22%20PM.png" alt="Screen Shot 2021-12-08 at 4.05.22 PM" style="zoom: 50%;" />

`dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])`
`dp[i][1] = max(dp[i-1][1], -prices[i])`

### ==无限次交易（不需要区分动作）==

`状态`：持有、不持有。（天数用一维、状态用一维）

`动作`：什么也不做、买、卖

DP 含义：拥有的价值`dp[i][j]`第i天状态j的价值

<img src="http://catbed.oss-cn-chengdu.aliyuncs.com/img/Screen%20Shot%202021-12-08%20at%204.13.08%20PM.png" alt="Screen Shot 2021-12-08 at 4.13.08 PM" style="zoom: 50%;" />

`dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])`
==`dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])`==

### ==2次交易（需要多一维区分动作）==

`状态`：持有、不持有。（天数用一维、状态用一维、==区分动作一维==）

`动作`：什么也不做、买、卖

DP 含义：拥有的价值`dp[i][j][k]`第i天区分j个动作状态k的价值

<img src="http://catbed.oss-cn-chengdu.aliyuncs.com/img/Screen%20Shot%202021-12-08%20at%204.54.01%20PM.png" alt="Screen Shot 2021-12-08 at 4.54.01 PM" style="zoom:33%;" />

```Python
dp[0][0][1] = -prices[0]
dp[0][1][1] = -prices[0]# 买了卖又买
# 第一次买入产生持有
dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
# 第一次卖出产生的不持有
dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1] + prices[i])
# 第二次买入产生的持有
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
# 第二次卖出产生的不持有
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
```

### ==k次交易（需要多一维区分动作）==

`状态`：持有、不持有。（天数用一维、状态用一维、==区分动作一维==）

`动作`：什么也不做、买、卖

DP 含义：拥有的价值`dp[i][j][k]`第i天区分j个动作状态k的价值

<img src="http://catbed.oss-cn-chengdu.aliyuncs.com/img/Screen%20Shot%202021-12-08%20at%205.19.03%20PM.png" alt="Screen Shot 2021-12-08 at 5.19.03 PM" style="zoom:33%;" />

```Python
# 0天 第k次买入产生持有状态设置
for i in range(k):
    dp[0][i][1] = -prices[0]

for i in range(1, len(prices)):
    # 第一次买入产生持有
    dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
    # 第一次卖出产生不持有
    dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1]+prices[i])
    for j in range(1, k):
        # 第j次买入产生持有 要看第j-1次卖出
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        # 第j次卖出产生持有 要看第j次买入
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
```

### ==不限次交易+有一天冻结期（状态+1）==

`状态`：持有、==不持有冻结、不持有不冻结==（天数用一维、状态用一维）

`动作`：什么也不做、买、卖、自然过渡

DP 含义：拥有的价值`dp[i][j]`第i天状态j的价值

<img src="http://catbed.oss-cn-chengdu.aliyuncs.com/img/Screen%20Shot%202021-12-08%20at%206.30.31%20PM.png" alt="Screen Shot 2021-12-08 at 6.30.31 PM" style="zoom:33%;" />

```Python
dp[0][0] = -prices[0]# 0持有 1不持有冻结 2不持有不冻结

for i in range(1, len(prices)):
    dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
    dp[i][1] = dp[i-1][0] + prices[i]
    dp[i][2] = max(dp[i-1][2], dp[i-1][1])

```

