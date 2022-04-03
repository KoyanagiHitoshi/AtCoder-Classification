C=int(input())
NML=[sorted(map(int,input().split())) for i in range(C)]
N,M,L=zip(*NML)
print(max(N)*max(M)*max(L))