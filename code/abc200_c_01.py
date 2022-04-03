N=int(input())
A=list(map(int,input().split()))
a=[0]*200
for i in range(N):
    a[A[i]%200]+=1
total=0
for i in range(200):
    total+=a[i]*(a[i]-1)//2
print(total)