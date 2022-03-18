# class LRUCache:
#     def __init__(self, capacity) -> None:
#         self.d = {}
#         self.capacity = capacity
#         self.order_l = []

#     def put(self, key, value):
#         if key in self.d:
#             self.order_l.remove(key)
#         elif len(self.order_l) == self.capacity:
#             name = self.order_l.pop(0)
#             self.d.pop(name)
            
#         self.d[key] = value
#         self.order_l.append(key)


#     def get(self, key):
#         if key in self.d:
#             self.order_l.remove(key)
#             self.order_l.append(key)
#             return self.d[key]
#         return -1


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.remove_node(node)
            self.add_node(node)
            return self.d[key].val
        else:
            return -1


    def put(self, key, val):
        if key in self.d:
            node = self.d[key]
            node.val = val
            self.remove_node(node)
            self.add_node(node)
        else:
            if len(self.d) < self.capacity:
                node = Node(key, val)
                self.d[key] = node
                self.add_node(node)
            else:
                node = Node(key, val)
                self.d[key] = node
                
                self.add_node(node)
                node = self.head.next
                self.d.pop(node.key)
                self.remove_node(self.head.next)


s = LRUCache(2)
s.put(1,1)
s.put(2,2)
s.get(1)
s.put(3,3)
s.get(2)
s.put(4,4)
s.get(1)
s.get(3)
s.get(4)
