import heapq
hq = [3, 2, 5, 1, 4]
print("list:", hq)
heapq.heapify(hq)
print("hq:", hq)
while hq:
    print("pop:", heapq.heappop(hq))
    print("hq:", hq)
