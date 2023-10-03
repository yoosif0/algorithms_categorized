class Stack:
    stack=[]

    def isEmpty(self):
        return len(self.stack) == 0 

    def pop(self):
        if self.isEmpty():
            raise ValueError("is empty")
        return self.stack.pop()
        
    def push(self, i):
        self.stack.append(i)

    def peek(self):
        if self.isEmpty():
            raise ValueError("is empty")
        return self.stack[-1]

ss = Stack()
ss.push("a")
ss.peek()
ss.push(3)
print(ss.pop())
    


