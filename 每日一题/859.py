class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        d_l = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                d_l.append(i)
        if len(s) != len(goal):
            return False
        if len(d_l) == 2 and s[d_l[0]] == goal[d_l[1]] and s[d_l[1]] == goal[d_l[0]]:
            return True
        if len(d_l) == 0 and len(set(s))<=len(s)-1 and len(s)!= 1:
            return True
        return False