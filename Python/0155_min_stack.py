class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
            return
        curr_min = self.stack[-1][1]
        self.stack.append((x, min(x, curr_min)))

    def pop(self):
        self.stack.pop()    

    def top(self):
        return self.stack[-1][0]    

    def getMin(self):
        return self.stack[-1][1]

if __name__ == "__main__":
    s = MinStack()
    s.push(3)
    s.push(7)
    s.push(-100)
    print(s.getMin())