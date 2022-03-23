from inspect import stack
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        s = []
        new_head = None

        p = head
        q = None
        while p:
            for _ in range(k):
                if not p:
                    if new_head:
                        q.next = s[0]
                        return new_head
                    return head
                s.append(p)
                p = p.next
            if not new_head:
                new_head = s[-1]

            
            for _ in range(k):
                q_next = s.pop()
                if q:
                    q.next = q_next
                q = q_next
        q.next = None
        return new_head

s = Solution()
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s.reverseKGroup(n1, 5)



