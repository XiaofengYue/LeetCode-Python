from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 层次遍历
        queue = [root]
        ans = []


        while queue:
            p = queue.pop(0)
            if p.left: queue.append(p.left)
            if p.right: queue.append(p.right)
            ans.append(p.val)
        
        return ans
