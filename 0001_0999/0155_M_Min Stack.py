class MinStack:

    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.min_data) == 0:
            self.min_data.append(val)
        else:
            self.min_data.append(min(val, self.min_data[-1]))

    def pop(self) -> None:
        if len(self.data) > 0:
            self.data.pop(-1)
            self.min_data.pop(-1)
        
    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]
        return None
        
    def getMin(self) -> int:
        if len(self.min_data) > 0:
            return self.min_data[-1]
        return None 
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()