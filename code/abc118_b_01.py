N,M=map(int,input().split())
A=[map(int,input().split()[1:]) for i in range(N)]
food=set(range(1,M+1))
for i in range(N):
    food&=set(A[i])
print(len(food))