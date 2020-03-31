N,K=map(int,input().split())
x=list(map(int,input().split()))
left=[0]*(N-K+1)
right=[0]*(N-K+1)
for i in range(len(left)):left[i]=abs(x[i])+abs(x[i+K-1]-x[i])
x=x[::-1]
for i in range(len(right)):right[i]=abs(x[i])+abs(x[i+K-1]-x[i])
print(min(min(left),min(right)))