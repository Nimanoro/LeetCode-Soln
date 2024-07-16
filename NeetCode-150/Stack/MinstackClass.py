class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and self.minstack[-1] < val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin()) # -3
    obj.pop()
    print(obj.top()) # 0
    print(obj.getMin()) # -2
    obj.push(-5)
    print(obj.getMin()) # -5