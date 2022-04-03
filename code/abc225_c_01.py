N,M=map(int,input().split())
B=[list(map(int,input().split())) for i in range(N)]
flag=True
for n in range(N):
    for m in range(M-1):
        if B[n][m+1]-B[n][m]==1 and 0<=(B[n][m]-1)%7<(B[n][m+1]-1)%7<=6:
            continue
        else:
            flag=False
for n in range(N-1):
    for m in range(M):
        if B[n+1][m]-B[n][m]==7:
            continue
        else:
            flag=False
print("Yes" if flag else "No")