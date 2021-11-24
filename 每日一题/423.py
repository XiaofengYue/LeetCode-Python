
# z -zero
# g - eight
# u - four
# w - two
# x - six

# o - one
# f - five
# s - seven
# i - nine
# t - three
from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        find_str = ['z', 'g', 'u', 'w', 'x', 'o', 'f', 's', 'i', 't']
        num_list = [0, 8, 4, 2, 6, 1, 5, 7, 9, 3]
        str_dic = {'z': 'zero', 'g':'eight', 'u':'four', 'w':'two', 'x':'six', 
                    'o':'one', 'f':'five', 's':'seven', 'i':'nine', 't':'three'}
        c = Counter(s)
        res = []
        for i in range(len(find_str)):
            if find_str[i] in c:
                n = c[find_str[i]]
                res.extend([num_list[i]] * n)
                c.subtract([i for i in str_dic[find_str[i]]]*n)
        res = sorted(res)
        return ''.join([str(n) for n in res])

s = Solution()
s.originalDigits("owoztneoer")