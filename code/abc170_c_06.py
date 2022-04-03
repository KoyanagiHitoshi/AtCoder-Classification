X,N=map(int,input().split())
p=list(map(int,input().split()))
m=100
for i in range(102):
    diff=abs(X-i)
    if i not in p and diff<m:
        ans=i
        m=diff
print(ans)