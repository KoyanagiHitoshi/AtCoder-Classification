N,L=map(int,input().split())
taste=[L+i for i in range(N)]
print(sum(taste)-min(taste,key=abs))