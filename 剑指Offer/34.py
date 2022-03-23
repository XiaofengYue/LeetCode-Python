from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        res = []
        def dfs(node: TreeNode, path: List):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and sum(path) == target: res.append(path[:])
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
n3 = TreeNode(3)
n2 = TreeNode(2)
n1 = TreeNode(1, n2, n3)
s = Solution()
s.pathSum(n1, 3)