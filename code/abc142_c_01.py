N=int(input())
A=list(map(int,input().split()))
sort=[0]*N
for i in range(N):
    sort[A[i]-1]+=i+1
print(*sort)