N,x=map(int,input().split())
A=list(map(int,input().split()))+[0]
count=0
for i in range(N):
    eated=max(0,A[i]+A[i-1]-x)
    count+=eated
    A[i]-=eated
print(count)