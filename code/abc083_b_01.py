n,a,b=map(int,input().split())
s=0
for i in range(n+1):
    c=0
    d=str(i)
    for j in range(len(d)):
        c+=int(d[j])
    if a<=c<=b:
        s+=i
print(s)