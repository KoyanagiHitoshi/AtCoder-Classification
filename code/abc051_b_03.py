K,S=map(int,input().split())
print(sum(0<=S-(Y+Z)<=K for Z in range(K+1) for Y in range(K+1)))