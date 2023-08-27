import heapq
hq = [3, 2, 5, 1, 4]
print("list:", hq)
heapq.heapify(hq)
print("hq:", hq)
print("pop:", heapq.heappushpop(hq, 6))
print("hq:", hq)
print("pop:", heapq.heappushpop(hq, 0))
print("hq:", hq)
