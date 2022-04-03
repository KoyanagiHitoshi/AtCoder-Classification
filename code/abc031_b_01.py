L,H=map(int,input().split())
N=int(input())
A=[int(input()) for i in range(N)]
for a in A:
    print(L-a if L>a else 0 if H>=a else -1)