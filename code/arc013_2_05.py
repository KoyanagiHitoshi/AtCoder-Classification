C=int(input())
NML=[sorted(map(int,input().split())) for i in range(C)]
N,M,L=map(max,zip(*NML))
print(N*M*L)