N,K,Q=map(int,input().split())
A=[int(input()) for i in range(Q)]
point=[0]*N
for a in A:
    point[a-1]+=1
for n in range(N):
    print("Yes" if point[n]>Q-K else "No")