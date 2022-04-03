N,M=map(int,input().split())
AB=[set(map(int,input().split())) for i in range(M)]
K=int(input())
CD=[tuple(map(int,input().split())) for i in range(K)]
ans=0
for bit in range(1<<K):
    ball=set()
    for k in range(K):
        if (bit>>k)&1:
            ball|={CD[k][1]}
        else:
            ball|={CD[k][0]}
    count=sum(ab<=ball for ab in AB)
    ans=max(ans,count)
print(ans)