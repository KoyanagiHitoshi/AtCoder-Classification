N,M,A,B=map(int,input().split())
for m in range(M):
    if N<=A:
        N+=B
    c=int(input())
    N-=c
    if N<0:
        print(m+1)
        break
else:
    print("complete")