class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, num):
        self.stack.append(num)
        if not self.maxStack or num >= self.maxStack[-1]:
            self.maxStack.append(num)

    def pop(self):
        if not self.stack:
            return None

        num = self.stack.pop()
        if num == self.maxStack[-1]:
            self.maxStack.pop()
        return num

    def getMax(self):
        if not self.maxStack:
            return None

        return self.maxStack[-1]