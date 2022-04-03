N,M=map(int,input().split())
AB=[tuple(map(int,input().split())) for i in range(M)]
K=int(input())
CD=[tuple(map(int,input().split())) for i in range(K)]
ans=0
for bit in range(1<<K):
    ball=set()
    for k in range(K):
        if (bit>>k)&1:
            ball.add(CD[k][1])
        else:
            ball.add(CD[k][0])
    count=sum(A in ball and B in ball for A,B in AB)
    ans=max(ans,count)
print(ans)