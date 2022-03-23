from typing import List
from collections import defaultdict
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
        ans = defaultdict(list)

        queue = [(1, root)]

        while queue:
            level, p = queue.pop(0)
            if p.left: queue.append((level+1, p.left))
            if p.right: queue.append((level+1, p.right))
            ans[level].append(p.val)
        return [v for k, v in ans.items()]
        print(ans)

