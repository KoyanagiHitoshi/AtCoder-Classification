N,M,C=map(int,input().split())
B=list(map(int,input().split()))
count=0
for i in range(N):
    A=list(map(int,input().split()))
    score=C
    for j in range(M):
        score+=A[j]*B[j]
    if score>0:
        count+=1
print(count)