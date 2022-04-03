N,W=map(int,input().split())
AB=sorted(list(map(int,input().split())) for i in range(N))[::-1]
total=0
for A,B in AB:
    total+=A*min(B,W)
    W-=min(W,B)
print(total)