# 寻找环的开头的问题。

## KEY
有O(1)的解法

## 思路

### Version 1
最简单的就是记住他们的ID 再次遇见就相当于有了环
```Python 
id_list = []
while id(head) not in id_list:
    if head == None:
        return None
    id_list.append(id(head))
    head = head.next
return head
```

### Version 2
使用双指针来快慢查找

```
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
```