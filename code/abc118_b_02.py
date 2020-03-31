n,m=map(int,input().split())
k=[0]*m
for i in range(n):
    A=[int(i) for i in input().split()]
    for i in range(1,len(A)):k[A[i]-1]+=1
print(sum(k[i]==n for i in range(m)))