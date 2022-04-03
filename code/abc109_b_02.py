N=int(input())
W=[input() for i in range(N)]
print("Yes" if len(set(W))==N and all(W[i-1][-1]==W[i][0] for i in range(1,N)) else "No")