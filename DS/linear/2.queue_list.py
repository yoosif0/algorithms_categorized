# Using pop while dequeuing take 0(n) time. This can be improved using an array or linkedlist

class Queue:
    q=[]

    def isEmpty(self):
        return len(self.q) == 0 

    def enqueue(self,i):
        self.q.append(i)
        
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("is empty")
        self.q.pop(0)

    def peek(self):
        if self.isEmpty():
            raise ValueError("is empty")
        return self.q[0]

    def display(self):
        print(self.q)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()

