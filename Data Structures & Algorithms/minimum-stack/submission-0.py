class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[-1]
        return None

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()