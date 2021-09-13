# 思路
解决两个问题：
1. 寻找子单词\
两个指针一起前进即可
2. 返回最长和字典序最小的
```Python
dictionary.sort() # 先排字典序列 第二优先级
dictionary.sort(key=lambda x:len(x), reverse=True)# 再排长度。第一优先级
```
## 代码
```Python
class Solution:
    def findLongestWord(self, s, dictionary):

        dictionary.sort()
        dictionary.sort(key=lambda x:len(x), reverse=True)



        for word in dictionary:
            ind_s,ind_w = 0,0

            while ind_s < len(s) and ind_w < len(word):
                if s[ind_s:ind_s+len(word)-ind_w] == word[ind_w:]:
                    return word
                if s[ind_s] == word[ind_w]:
                    ind_s += 1
                    ind_w += 1
                else:
                    ind_s += 1
            if ind_w==len(word):
                return word 
        return ''
```