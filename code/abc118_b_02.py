N,M=map(int,input().split())
food=set(range(1,M+1))
for i in range(N):
    K,*A=map(int,input().split())
    food&=set(A)
print(len(food))