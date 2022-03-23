from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (root and not root.left and not root.right):
            return True

        def judge(A: TreeNode, B:TreeNode):
            if not A and not B: return True
            if (not A and B) or (not B and A): return False
            return (A.val == B.val) and judge(A.left, B.right) and judge(A.right, B.left)
        
        if root.left and root.right:
            return judge(root.left, root.right)
        return False
