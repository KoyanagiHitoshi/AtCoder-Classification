K,S=map(int,input().split())
print(sum(1 for Z in range(K+1) for Y in range(K+1) if 0<=S-(Y+Z)<=K))