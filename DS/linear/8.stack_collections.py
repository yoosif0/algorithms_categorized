from collections import deque

s = deque()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
print(list(s))
print(s.pop())
print(list(s))
s.append("a")
print(list(s))
print(s[-1])
 

