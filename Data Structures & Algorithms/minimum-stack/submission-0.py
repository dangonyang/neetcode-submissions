class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []
        self.mini = float

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minstk or val < self.minstk[-1]:
            self.minstk.append(val)
        else:
            self.minstk.append(self.minstk[-1])
        

    def pop(self) -> None:
        del self.stk[-1]
        del self.minstk[-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
