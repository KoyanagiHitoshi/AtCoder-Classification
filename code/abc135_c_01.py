N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
for i in range(N):
    count+=min(A[i],B[i])
    if A[i]<B[i]:
        if A[i+1]<B[i]-A[i]:
            count+=A[i+1]
            A[i+1]=0
        else:
            count+=B[i]-A[i]
            A[i+1]-=B[i]-A[i]
print(count)