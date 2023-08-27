from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")
print(queue)
queue.popleft()
print(queue)
