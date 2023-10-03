class Node():
    next
    def __init__(self, val):
        self.val = val


class Stack:
    top = None

    def isEmpty(self):
        return self.top is None

    def pop(self):
        if self.isEmpty():
            return "is empty"
        val = self.top.val
        self.top = self.top.next
        return val
        
    def push(self, val):
        oldVal = self.top
        self.top = Node(val)
        self.top.next = oldVal

    def peek(self):
        if self.isEmpty():
            return "is empty"
        return self.top.val



s = Stack()
s.push("a")
print(s.top.val)
s.push(1)
print(s.top.val)
s.push(0)
print(s.top.val)
s.push(2)
print(s.top.val)
print(s.pop())
print(s.top.val)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())