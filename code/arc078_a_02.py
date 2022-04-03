N=int(input())
a=list(map(int,input().split()))
total=sum(a)
A=[0]*N
for i in range(N-1):
    A[i+1]=A[i]+a[i]
print(min(abs(total-2*A[i]) for i in range(1,N)))