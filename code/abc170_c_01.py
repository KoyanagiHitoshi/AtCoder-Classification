X,N=map(int,input().split())
p=list(map(int,input().split()))
diff=102
for i in range(102):
    if i not in p and abs(X-i)<diff:
        diff=abs(X-i)
        ans=i
print(ans)