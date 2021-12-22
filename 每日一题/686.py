'''
Description: 
Author: yxf
Date: 2021-12-22 09:35:01
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        return l if (a * (l:=ceil(len(b)/len(a)))).find(b) != -1 else l + 1 if (a * (l + 1)).find(b) != -1 else -1
