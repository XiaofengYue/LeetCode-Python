from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue_stack = [root]
        # 1 3 5 7 9 queue 2 4 6 8 10 stack
        queue_flag = True
        ans = []

        while queue_stack:
            level_l = []
            level_length = len(queue_stack)
            for _ in range(level_length):
                p = queue_stack.pop(0)
                if p.left: queue_stack.append(p.left)
                if p.right: queue_stack.append(p.right)
                if queue_flag:
                    level_l.append(p.val)
                else:
                    level_l.insert(0, p.val)
            ans.append(level_l)
            queue_flag = not queue_flag
        
        return ans
