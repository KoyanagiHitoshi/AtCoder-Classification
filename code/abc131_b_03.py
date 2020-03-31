N,L=map(int,input().split())
l=range(L,L+N)
print(sum(l)-min(l,key=abs))