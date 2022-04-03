N=int(input())
A=list(map(int,input().split()))[::-1]
total=0
for i in range(N):
    total+=A[i]*2**i
print(total)