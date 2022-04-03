N,L=map(int,input().split())
taste=range(L,L+N)
print(sum(taste)-min(taste,key=abs))