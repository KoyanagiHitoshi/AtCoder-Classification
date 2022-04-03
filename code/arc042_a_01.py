N,M=map(int,input().split())
A=[int(input()) for i in range(M)][::-1]
board=[]
written=set()
for thread in A:
    if thread not in written:
        board.append(thread)
    written.add(thread)
for thread in range(1,N+1):
    if thread not in written:
        board.append(thread)
print(*board,sep="\n")