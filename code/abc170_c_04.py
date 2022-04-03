X,N=map(int,input().split())
p=list(map(int,input().split()))
diff=99
for x in range(102):
    if x not in p and abs(X-x)<diff:
        diff=abs(X-x)
        ans=x
print(ans)