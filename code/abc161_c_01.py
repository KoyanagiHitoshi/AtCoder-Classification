N,K=map(int,input().split())
print(min(N%K,abs(K-N%K)))