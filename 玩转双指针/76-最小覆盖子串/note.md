# 思想
两个指针确定一个窗口。
寻找最小的窗口来符合我们的题目要求。
1. r指针向右滑动(遍历完)
    如果找到个窗口符合题目要求时进行如下操作
        1.1 左边指针从左向右扫过。
            如果左边指针使最小窗口不成立时  回到第一步
白话：先找到一个窗口。然后从左到右缩小窗口，缩小到第一次不满足要求时（也就是多删除了一个指定的符号）。再次向右扫描到符合窗口。
## 代码
```Python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        res = 0
        l = 0
        min_len = len(s) + 1
        min_l = 0

        for char in t:
            dic[char] = dic.get(char, 0) + 1

        for r in range(0, len(s)):
            if s[r] in dic:
                dic[s[r]] -= 1
                if dic[s[r]] >= 0:
                    res += 1
                
                # 匹配完全之后再挪动左边
                while res == len(t):
                    if (r - l + 1 < min_len):
                        min_l = l
                        min_len = r - l + 1
                    if s[l] in dic :
                        dic[s[l]] += 1
                        if dic[s[l]] > 0:
                            res -= 1
                    l+=1

        return '' if min_len > len(s) else s[min_l:min_l+min_len]
```