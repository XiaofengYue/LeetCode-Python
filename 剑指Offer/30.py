from typing import List

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_helper = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stack_helper and x > self.stack_helper[-1]:
            self.stack_helper.append(self.stack_helper[-1])
        else:
            self.stack_helper.append(x)


    def pop(self) -> None:
        self.stack.pop()
        self.stack_helper.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.stack_helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()