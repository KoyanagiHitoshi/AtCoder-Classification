N=int(input())
S=[input() for i in range(N)]
degree=[[0,1],[1,0],[1,1],[1,-1]]
def judge(x,y):
    if 0<=x<=N-1 and 0<=y<=N-1:
        return S[x][y]=="#"
    return -6
for x in range(N):
    for y in range(N):
        for dx,dy in degree:
            if sum(judge(x+dx*dist,y+dy*dist) for dist in range(6))>=4:
                print("Yes")
                exit()
print("No")