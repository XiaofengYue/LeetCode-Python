
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

None if min_len > len(s) else s[min_l:min_l+min_len]
