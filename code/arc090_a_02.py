N=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
count=0
for i in range(N):
    count=max(count,sum(A1[:i+1])+sum(A2[i:]))
print(count)