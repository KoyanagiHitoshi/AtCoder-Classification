N,K=map(int,input().split())
a=list(map(int,input().split()))
print(sum(a[i]*min(i+1,K,N-i,N-K+1) for i in range(N)))