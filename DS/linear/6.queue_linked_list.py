class Node():
    next
    def __init__(self, val):
        self.val = val


class Queue:
    head = None
    tail = None

    def isEmpty(self):
        return self.head is None

    def dequeue(self):
        if self.isEmpty():
            return ValueError("is empty")
        val = self.head.val
        self.head = self.head.next
        return val
        
    def enqueue(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
            return
        self.tail.next = newNode
        self.tail = newNode

    def peek(self):
        if self.isEmpty():
            return ValueError("is empty")
        return self.head.val



s = Queue()
s.enqueue("a")
print(s.peek())
s.enqueue(1)
s.enqueue(0)
print(s.peek())
s.enqueue(2)
print(s.dequeue())
print(s.peek())