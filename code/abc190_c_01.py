import itertools
N,M=map(int,input().split())
AB=[tuple(map(int,input().split())) for i in range(M)]
K=int(input())
CD=[tuple(map(int,input().split())) for i in range(K)]
ans=0
for ball in itertools.product(*CD):
    count=sum(A in ball and B in ball for A,B in AB)
    ans=max(ans,count)
print(ans)