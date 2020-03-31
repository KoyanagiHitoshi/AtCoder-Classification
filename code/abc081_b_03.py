n=int(input())
A=list(map(int,input().split()))
ans=0
while all(a%2==0 for a in A):
    for i in range(n):
        A[i]=A[i]/2
    ans+=1
print(ans)