N,M,C=map(int,input().split())
B=list(map(int,input().split()))
count=0
for i in range(N):
    A=list(map(int,input().split()))
    if sum(a*b for a,b in zip(A,B))+C>0:count+=1
print(count)