# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        def dfs(head):
            if head == None:
                return
            dfs(head.next)
            val = head.val
            res.append(val)
        
        dfs(head)

        return res