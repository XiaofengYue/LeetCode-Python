# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.calcu(root)
        return self.ans

    def calcu(self, node):
        if node is None:
            return 0
        else:
            left = self.calcu(node.left)
            right = self.calcu(node.right)
            self.ans += abs(left - right)
            return left + right + node.val

s = Solution()
left = TreeNode(2)
right = TreeNode(3)
root = TreeNode(1,left,right)
s.findTilt(root)