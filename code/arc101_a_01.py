n,k=map(int,input().split())
x=sorted(list(map(int,input().split())))
a=[]
for i in range(n-k+1):
    l=x[i]
    r=x[i+k-1]
    a.append(min(abs(l)+abs(r-l),abs(r)+abs(l-r)))
print(min(a))