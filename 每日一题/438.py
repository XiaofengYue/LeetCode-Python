from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 做个映射 数组方便统计
        dic = defaultdict(int)
        for i in p:
            dic[i] += 1
        match = 0
        match_all = len(p)
        ans = []
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            if s[i] in dic :
                dic[s[i]] -= 1
                match += 1
        
        left = 0
        for right in range(len(p), len(s)):
            if match == match_all and set(dic.values()) == {0}:
                ans.append(left)
            # 处理左边
            if s[left] in dic:
                dic[s[left]] += 1
                match -= 1
            # 处理右边
            if s[right] in dic:
                dic[s[right]] -= 1
                match += 1
            left += 1
        if match == match_all and set(dic.values()) == {0}:
            ans.append(left)
        return ans
s = Solution()
s.findAnagrams(s = "abacbabc", p = "abc")
