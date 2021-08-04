'''
# Min stack (Uber)

Design a simple stack that supports push, pop, top and retrieving the minimum element in constant time. 

push(x)     -- Push element x onto stack
pop()       -- Removes the elemento on top of the stack
top()       -- Get the top element
getMin()    -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called on an empty stack.
'''

class minStack(object):
    def __init__(self):
        self.stack = []
        self.mins  = []

    def push(self, x):
        self.stack.append(x)
        if len(self.mins) == 0:
            self.mins.append(x)
        else:
            self.mins.append(min(self.getMin(), x))

    def pop(self):
        if len(self.stack) == 0: 
            return None
        else:
            self.mins.pop()
            return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        if len(self.mins) == 0:
            return None
        else:
            return self.mins[-1]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
