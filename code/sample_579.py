import heapq
hq = [3, 2, 5, 1, 4]
print("list:", hq)
heapq.heapify(hq)
print("hq:", hq)
heapq.heappush(hq, 6)
print("push 6:", hq)
heapq.heappush(hq, 0)
print("push 0:", hq)
