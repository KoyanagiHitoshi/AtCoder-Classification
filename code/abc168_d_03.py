from collections import deque
N,M=map(int,input().split())
graph=[[] for i in range(N)]
for m in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
queue=deque([0])
distance=[0]*N
while queue:
    room=queue.popleft()
    for next_room in graph[room]:
        if distance[next_room]==0:
            distance[next_room]=room+1
            queue.append(next_room)
if 0 in distance:
    print("No")
else:
    print("Yes")
    print(*distance[1:],sep="\n")