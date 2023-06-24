class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  
print(stack.isEmpty())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())
print(stack.pop())
