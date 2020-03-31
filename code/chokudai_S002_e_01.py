n=int(input())
ans=0
for i in range(n):
    a,b=map(int,input().split())
    ans+=min(a//2,b)
print(ans)