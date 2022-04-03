N,K=map(int,input().split())
H=sorted(map(int,input().split()))[::-1]
print(sum(H[K:]))