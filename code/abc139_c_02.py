N=int(input())
H=list(map(int,input().split()))
h=[0]*N
for i in range(1,N):
    if H[i-1]>=H[i]:
        h[i]=h[i-1]+1
print(max(h))