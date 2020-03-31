X=int(input())
d=X//11*2
m=X%11
if m>0:d+=1
if m>6:d+=1
print(d)