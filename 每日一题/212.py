# 思路清晰

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

w, h = len(board[0]), len(board)

eles = [ch for word in board for ch in word]

# 每个元素需要存放相邻元素的信息(或者位置)

def get_neighbor(pos):
    neighs = []
    if pos%w != 0: # 有左
        neighs.append(pos-1)
    if pos//w != 0: # 有上
        neighs.append(pos-w)
    if pos%w != w-1: # 有右
        neighs.append(pos+1)
    if pos//w != h-1: # 有下
        neighs.append(pos+w)
    return neighs

# 单词的开头 我们需要用字典存放(方便找到开头)
from collections import defaultdict

start_word_dic = defaultdict(list)
for i, ch in enumerate(eles):
    start_word_dic[ch].append(i)

# 每个用过的单词我们需要用标记来确定他不再被复用
book = [0 for i in eles]


# 查找单词的过程应该是个dfs的过程

def dfs(word):
    
