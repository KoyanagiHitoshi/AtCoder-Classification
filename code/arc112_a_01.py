T=int(input())
for i in range(T):
    L,R=map(int,input().split())
    n=max(R-2*L+1,0)
    print(n*(n+1)//2)