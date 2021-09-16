# 思路
也就是从0-x每次都二分查找即可
# 代码
```Python
class Solution:
    def mySqrt(self, x: int) -> int:

        l, r =0, x

        while l <= r:
            mid = (l+r)//2 

            res = pow(mid,2)
            if res > x:
                r = mid - 1
            elif res == x:
                return mid
            else:
                if pow(mid+1, 2) > x:
                    return mid
                else:
                    l = mid + 1
```