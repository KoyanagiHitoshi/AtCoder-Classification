N=int(input())
A=sorted(map(int,input().split()))
MAX=A[-1]
divisor=[0]*(MAX+1)
for a in A:
    if divisor[a]!=0:
        divisor[a]=2
    for i in range(a,MAX+1,a):
        divisor[i]+=1
count=0
for a in A:
    if divisor[a]==1:
        count+=1
print(count)