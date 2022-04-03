a,b,c,x=[int(input()) for i in range(4)]
x//=50
p=min(a,x//10)
ans=0
for i in range(p+1):
    y=x-10*i
    q=min(b,y//2)
    for j in range(q+1):
        z=y-2*j
        if c>=z:ans+=1
print(ans)