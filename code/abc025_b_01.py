N,A,B=map(int,input().split())
position=0
for i in range(N):
    s,d=input().split()
    d=int(d)
    if s=="East":
        if d<A:
            d=A
        if d>B:
            d=B
    else:
        if d<A:
            d=A
        if d>B:
            d=B
        d=-d
    position+=d
print("0" if position==0 else "East "+str(position) if position>0 else "West "+str(abs(position)))