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

s = Solution()
s.findLongestWord("foobarfoobar", ["foo","bar"])