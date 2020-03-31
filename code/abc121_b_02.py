N,M,C=map(int,input().split())
B=list(map(int,input().split()))
count=0
for i in range(N):
    A=list(map(int,input().split()))
    p=C
    for j in range(M):p+=A[j]*B[j]
    if p>0:count+=1
print(count)