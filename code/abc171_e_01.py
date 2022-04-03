N=int(input())
a=list(map(int,input().split()))
X=0
for i in range(N):
    X=X^a[i]
xor=[X]*N
for i in range(N):
    xor[i]^=a[i]
print(*xor)