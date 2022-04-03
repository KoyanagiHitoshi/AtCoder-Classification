from collections import deque
R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
c=[list(input()) for i in range(R)]
visited=[[-1]*C for r in range(R)]
visited[sy-1][sx-1]=0
queue=deque([[sy-1,sx-1]])
direction=[[0,1],[1,0],[0,-1],[-1,0]]
while queue:
    y,x=queue.popleft()
    if [y,x]==[gy-1,gx-1]:
        print(visited[y][x])
    for dy,dx in direction:
        next_y,next_x=y+dy,x+dx
        if c[next_y][next_x]=="." and visited[next_y][next_x]==-1:
            visited[next_y][next_x]=visited[y][x]+1
            queue.append([next_y,next_x])