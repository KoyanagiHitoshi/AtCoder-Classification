import numpy as np
N=int(input())
x=list(map(int,input().split()))
m=y=c=0
for i in range(N):
    m+=abs(x[i])
print(m)
for i in range(N):
    y+=x[i]**2
print(y**.5)
X=[]
for i in range(N):
    X.append(abs(x[i]))
print(max(X))
