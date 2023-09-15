class Stack:
    def __init__(self, k):
        self.s = [None] * k 
        self.top = -1
        self.k = k

    def isEmpty(self):
        return self.top == -1 
    
    def isFull(self):
        return self.top == self.k - 1

    def pop(self):
        if self.isEmpty():
            raise TypeError("is empty")
        val = self.s[self.top]
        self.s[self.top] = None
        self.top = self.top - 1
        return val
        
    def push(self, i):
        if self.isFull():
            raise TypeError("is full")
        self.top = self.top + 1
        self.s[self.top] = i

    def peek(self):
        if self.isEmpty():
            raise TypeError("is empty")
        return self.s[self.top]

ss = Stack(4)
ss.push("a")
print(ss.s)
ss.push("b")
ss.push("c")
ss.push("d")
# ss.push("f")
print(ss.s)
print(ss.peek())
print(ss.pop())
print(ss.s)
print(ss.pop())
print(ss.s)
print(ss.pop())
print(ss.s)
print(ss.pop())
print(ss.s)
# print(ss.pop())
# print(ss.s)
