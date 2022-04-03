N,X=map(int,input().split())
L=list(map(int,input().split()))
for i in range(N-1):
    L[i+1]+=L[i]
count=1
for i in range(N):
    if L[i]<=X:
        count+=1
print(count)