N=int(input())
A,B,C=[list(map(int,input().split())) for i in range(3)]
satisfaction=0
for i in range(N):
    satisfaction+=B[A[i]-1]
    if i!=0 and A[i]==A[i-1]+1:
        satisfaction+=C[A[i-1]-1]
print(satisfaction)