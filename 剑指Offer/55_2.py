from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def recur(root:TreeNode):
            if not root:
                return 0
            l, r = recur(root.left), recur(root.right)
            if l==-1 or r == -1 or abs(l-r)>1:  return -1
            return 1+max(l, r)
        
        return recur(root)

