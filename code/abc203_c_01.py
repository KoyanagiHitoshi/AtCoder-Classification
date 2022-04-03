N,K=map(int,input().split())
AB=sorted(list(map(int,input().split())) for i in range(N))
for A,B in AB:
    if A<=K:
        K+=B
print(K)