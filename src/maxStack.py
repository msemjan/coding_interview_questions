import sys

class MaxStack:
    stack = None
    max_stack = None

    def __init__(self):
        # Fill this in.
        self.stack = list()
        self.max_stack = [-sys.maxsize]

    def push(self, val):
        # Fill this in.
        self.stack.append(val)

        if val > self.max_stack[-1]:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        # Fill this in.
        self.max_stack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def max(self):
        # Fill this in.
        if len(self.stack) == 0:
            return None
        else:
            return self.max_stack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2

