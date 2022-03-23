from operator import le
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        left, right = head, head
        for _ in range(k):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        return left