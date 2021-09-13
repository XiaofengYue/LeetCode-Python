# 思路
很明显用两个指针指向前后来向中间搜索
## 代码
```Python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def judge(s, chance = 1):
            i, j = 0, len(s) - 1
            while i < j :
                if s[i] != s[j]:
                    if chance == 1:
                        if judge(s[i+1:j+1], chance=0) or judge(s[i:j], chance=0):
                            return True
                    return False
                i += 1
                j -= 1
            return True
        return judge(s)

s = Solution()
print(s.validPalindrome("ebcbbececabbacecbbcbe"))
```