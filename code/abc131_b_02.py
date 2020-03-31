N,L=map(int,input().split())
cumulative=[L+i for i in range(N)]
print(sum(cumulative)-min(cumulative,key=abs))