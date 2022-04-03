N,W=map(int,input().split())
AB=[]
for i in range(N):
    A,B=map(int,input().split())
    AB.append([A,B])
AB.sort(reverse=True)
total=0
for A,B in AB:
    total+=A*min(B,W)
    W-=min(W,B)
print(total)