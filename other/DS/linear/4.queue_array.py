class Queue:

    def __init__(self, k):
        self.q = [None] * k 
        self.head = None
        self.tail = 0
        self.k = k

    def isEmpty(self):
        return self.q[self.head] == None 

    def isFull(self):
        return self.head == self.tail

    def enqueue(self,item):
        if self.isFull():
            raise TypeError("cant. the queue is full")
        self.q[self.tail] = item 
        self.tail = 0 if self.tail == self.k - 1 else self.tail + 1
        if self.head is None:
            self.head = 0
        
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("cant. the queue is empty")
        val = self.q[self.head]
        self.q[self.head] = None
        self.head = 0 if self.head == self.k - 1 else self.head + 1
        return val
         

    def peek(self):
        if self.isEmpty():
            raise ValueError("cant. the queue is empty")
        return self.q[self.head]

    def display(self):
        print(self.q)


q = Queue(5)
q.enqueue(1)
q.display()
q.enqueue(2)
q.display()
q.enqueue(3)
q.display()
q.enqueue(4)
q.display()
q.enqueue(5)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.enqueue("s")
q.display()
q.enqueue("s")
q.display()
q.dequeue()
q.display()