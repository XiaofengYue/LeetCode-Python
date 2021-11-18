# from collections import defaultdict
# class Solution(object):
#     def maxProduct(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """

#         graph = [[0 for i in range(len(words))]for j in range(len(words))]

#         for ch in [chr(i) for i in range(ord("a"),ord("z")+1)]:
#             similar_ch = []
#             for i in range(len(words)):
#                 if ch in words[i]:
#                     similar_ch.append(i)
#             for i in similar_ch:
#                 for j in similar_ch:
#                     graph[i][j] = 1
#                     graph[j][i] = 1
        
#         res = 0
#         for w1 in range(len(graph)):
#             for w2 in range(len(graph)):
#                 if graph[w1][w2] == 0:
#                     res = max(res, len(words[w1])*len(words[w2]))
#         print(res)


# 位运算方式

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        binary_words = [sum(1<<(ord(c) - ord('a')) for c in set(word)) for word in words]
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not binary_words[i] & binary_words[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))