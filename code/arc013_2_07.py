C=int(input())
N,M,L=zip(*[sorted(map(int,input().split())) for i in range(C)])
print(max(N)*max(M)*max(L))