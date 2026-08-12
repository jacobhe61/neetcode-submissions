class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or val < self.mins[len(self.mins)-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[len(self.mins)-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]