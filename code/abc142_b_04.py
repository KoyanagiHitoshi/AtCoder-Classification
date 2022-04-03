N,K=map(int,input().split())
H=list(map(int,input().split()))
print(sum(1 for h in H if h>=K))