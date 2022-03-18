from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i, j =0, 0
        d = {}
        for j in range(0, len(s)): # 左闭右闭
            substr = s[i:j]
            
            # print('its turn:{}'.format(s[j]))
            if s[j] not in substr:
                res = max(res, j+1-i)
                d[s[j]] = j
                # print(res)
                # print(s[i:j+1])
            else:
                i = d[s[j]] + 1
                d[s[j]] = j
            j += 1
        return res