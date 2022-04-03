N=int(input())
A=list(map(int,input().split()))
count=0
while all(a%2==0 for a in A):
    for i in range(N):
        A[i]=A[i]/2
    count+=1
print(count)