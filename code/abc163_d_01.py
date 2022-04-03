N,K=map(int,input().split())
total=0
for k in range(K,N+2):
    diff=k*(2*N-k+1)//2-k*(k-1)//2
    total=(total+diff+1)%(10**9+7)
print(total)