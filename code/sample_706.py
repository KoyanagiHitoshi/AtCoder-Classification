import queue
q = queue.LifoQueue()
x = [3, 4, 5]
for i in x:
    q.put(i)
while not q.empty():
    print(q.get())
