N,va,vb,L=map(int,input().split())
for i in range(N):
    time=L/va
    L=vb*time
print(L)