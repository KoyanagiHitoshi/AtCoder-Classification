import heapq
hq = [3, 2, 5, 1, 4]
print("list:", hq)
heapq.heapify(hq)
print("hq:", hq)
print("pop:", heapq.heapreplace(hq, 6))
print("hq:", hq)
print("pop:", heapq.heapreplace(hq, 0))
print("hq:", hq)
