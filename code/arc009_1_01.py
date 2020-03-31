N=int(input())
ans=0
for i in range(N):
    a,b=map(int,input().split())
    ans+=-(-a*b*1.05)
print(int(ans))