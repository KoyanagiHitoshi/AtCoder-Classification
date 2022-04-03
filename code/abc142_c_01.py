N=int(input())
A=list(map(int,input().split()))
students=[0]*N
for i in range(N):
    students[A[i]-1]+=i+1
print(*students)