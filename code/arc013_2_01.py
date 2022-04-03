C=int(input())
n,m,l=0,0,0
for i in range(C):
    N,M,L=sorted(map(int,input().split()))
    n,m,l=max(n,N),max(m,M),max(l,L)
print(n*m*l)