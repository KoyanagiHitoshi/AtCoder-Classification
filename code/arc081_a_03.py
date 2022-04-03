import heapq
N=int(input())
A=list(map(int,input().split()))
edge=set()
queue=[0,0]
for a in A:
    if a>queue[0]:
        try:
            edge.remove(a)
            heapq.heapreplace(queue,a)
        except:
            edge.add(a)
print(queue[0]*queue[1])