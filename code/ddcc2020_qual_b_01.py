N=int(input())
A=list(map(int,input().split()))
total=sum(A)
cost=total
cumulative=0
for i in range(N):
    cumulative+=A[i]
    cost=min(cost,abs(cumulative-(total-cumulative)))
print(cost)