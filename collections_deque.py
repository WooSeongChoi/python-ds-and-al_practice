from collections import deque

q = deque(["버피", "잰더", "월로"])
print(q)

q.append("자일스")
print(q)

q.appendleft("엔젤")
print(q)

q.pop()
print(q)

q.popleft()
print(q)

q.rotate(1)
print(q)

q.rotate(-1)
print(q)

q = deque(range(10))
print(q)

q.rotate(5)
print(q)

q.rotate(-4)
print(q)