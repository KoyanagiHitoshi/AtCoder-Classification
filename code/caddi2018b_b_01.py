N,H,W=map(int,input().split())
board=0
for i in range(N):
    A,B=map(int,input().split())
    if H<=A and W<=B:
        board+=min(A//H,B//W)
print(board)