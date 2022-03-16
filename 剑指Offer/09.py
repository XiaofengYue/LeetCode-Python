from typing import List

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack2.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())



    def deleteHead(self) -> int:
        if not self.stack1 : return -1
        return self.stack1.pop()


