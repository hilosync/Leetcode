class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)
        self.minStack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.min = self.minStack[-1] if self.minStack else float("inf")
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()