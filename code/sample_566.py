import collections
queue = collections.deque(["a", "b", "c"])
queue.append("d")
print(queue)
queue.popleft()
print(queue)
