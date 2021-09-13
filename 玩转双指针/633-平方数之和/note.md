# 思路

跟同一个数组搜索两个数字一样的套路。向中间逼近

## 代码

```Python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = math.ceil(math.sqrt(c))

        while i<=j:
            sum = pow(i,2) + pow(j,2)
            if sum == c:
                return True
            if sum > c:
                j -= 1
            else:
                i += 1

        return False
```