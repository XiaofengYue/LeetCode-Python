class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ### Version 1 ###
        # id_list = []
        # while id(head) not in id_list:
        #     if head == None:
        #         return None
        #     id_list.append(id(head))
        #     head = head.next
        # return head

        ### Version 2 ###
        if head == None or head.next == None or head.next.next == None:
            return None
        fast = head.next.next
        slow = head.next

        # 寻找碰面点
        while fast != slow:
            if fast.next == None or fast.next.next ==None:
                return None
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        # 寻找环的起点
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow





n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

s = Solution()
s.detectCycle(n1)


print (1)