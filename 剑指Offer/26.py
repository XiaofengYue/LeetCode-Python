from trace import Trace
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def judge(p: TreeNode, q:TreeNode):
            if not q:   return True
            if not p or p.val != q.val: return False
            return judge(p.left, q.left) and judge(p.right, q.right)


        return bool(A and B) and (judge(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))