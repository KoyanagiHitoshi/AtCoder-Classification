N=int(input())
A=list(map(int,input().split()))
money=1000
for i in range(N-1):
    if A[i]<A[i+1]:
        stock=money//A[i]
        money+=(A[i+1]-A[i])*stock
print(money)