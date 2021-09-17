# 思路清晰
from collections import defaultdict

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]

w, h = len(board[0]), len(board)

eles = [ch for word in board for ch in word]
res = set()

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

char_pos_dic = defaultdict(list)
for i, ch in enumerate(eles):
    char_pos_dic[ch].append(i)



def dfs(word_to_pos, now, next):
    if next == len(word_to_pos):
        print('匹配成功')
    


# example 


for word in words:
    word_to_pos = []
    for char in word:
        if char in char_pos_dic:
            word_to_pos.append(char_pos_dic[char])
        else:
            break
    
    if len(word_to_pos) == len(word): # 所有单词都有哦
        
        while 
