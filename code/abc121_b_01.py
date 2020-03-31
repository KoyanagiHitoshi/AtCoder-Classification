N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(N)]
count=0
for a in A:
    p=0
    for i in range(M):
        p+=a[i]*B[i]
    p+=C
    if p>0:count+=1
print(count)