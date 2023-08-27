import queue
q = queue.Queue()
x = [3, 4, 5]
for i in x:
    q.put(i)
while not q.empty():
    print(q.get())
