from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(list(q))

q.popleft()

print("After removing an element")
print(list(q))


