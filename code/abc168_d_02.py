from collections import deque
N,M=map(int,input().split())
graph=[[] for i in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
queue=deque([0])
distance=[0]*N
while queue:
    que=queue.popleft()
    for value in graph[que]:
        if distance[value]==0:
            distance[value]=que+1
            queue.append(value)
if 0 in distance:
    print("No")
else:
    print("Yes")
    for i in range(1,N):
        print(distance[i])