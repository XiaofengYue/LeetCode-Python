from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        p, q = head, head.next

        while q:
            if q.val == val:
                p.next = q.next
                break
            p = p.next
            q = q.next
        return head