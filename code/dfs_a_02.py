from collections import deque

H,W=map(int,input().split())
c=[input() for i in range(H)]

flag=[[False]*W for i in range(H)]
moves=[[0,1],[1,0],[0,-1],[-1,0]]

def dfs(start_i,start_j):
    flag[start_i][start_j]=True
    stack=deque([[start_i,start_j]])
    while stack:
        h,w=stack.pop()
        if c[h][w]=="g":
            return "Yes"
        for move in moves:
            i,j=h+move[0],w+move[1]
            if not(0<=i<H) or not(0<=j<W) or c[i][j]=="#" or flag[i][j]:
                continue
            elif c[i][j]!="#" and not(flag[i][j]):
                flag[i][j]=True
                stack.append([i,j])
    return "No"

for i in range(H):
    for j in range(W):
        if c[i][j]=="s":
            start_i,start_j=i,j
            break

print(dfs(start_i,start_j))