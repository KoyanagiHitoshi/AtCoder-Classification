import sys
sys.setrecursionlimit(10**6)

H,W=map(int,input().split())
c=[input() for i in range(H)]

flag=[[False]*W for i in range(H)]
moves=[[0,1],[1,0],[0,-1],[-1,0]]

def dfs(i,j):
    if not(0<=i<H) or not(0<=j<W) or c[i][j]=="#" or flag[i][j]:
        return
    flag[i][j]=True
    for move in moves:
        dfs(i+move[0],j+move[1])

for i in range(H):
    for j in range(W):
        if c[i][j]=="s":
            start_i,start_j=i,j
        if c[i][j]=="g":
            goal_i,goal_j=i,j

dfs(start_i,start_j)
print("Yes" if flag[goal_i][goal_j] else "No")