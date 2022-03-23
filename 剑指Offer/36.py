from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 思路应该时中序遍历
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':# 


        def dfs(node: Node):
            if not node:    return
            dfs(node.left)
            if not self.pre:    
                self.pre = node
                self.cur = node
            else:
                self.cur.right = node
                node.left = self.cur
                self.cur = node
            dfs(node.right)

        if not root:    return
        self.pre = None
        dfs(root)
        self.pre.left, self.cur.right = self.cur, self.pre
        return self.pre