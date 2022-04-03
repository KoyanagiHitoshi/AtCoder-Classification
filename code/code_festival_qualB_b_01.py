N,K=map(int,input().split())
a=[int(input()) for i in range(N)]
total=0
for i in range(N):
    total+=a[i]
    if total>=K:
        print(i+1)
        break