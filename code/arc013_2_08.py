C=int(input())
N,M,L=map(max,zip(*[sorted(map(int,input().split())) for i in range(C)]))
print(N*M*L)