N,K=map(int,input().split())
x=list(map(int,input().split()))
n=N-K+1
left=[0]*n
for i in range(n):left[i]=abs(x[i])+abs(x[i]-x[i+K-1])
x=x[::-1]
right=[0]*n
for i in range(n):right[i]=abs(x[i])+abs(x[i]-x[i+K-1])
print(min(min(left),min(right)))