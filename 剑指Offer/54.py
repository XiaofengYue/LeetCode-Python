from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def in_order(root):
            if not root:    return []
            return in_order(root.left) + [root.val] + in_order(root.right)

        return in_order(root)[-k]