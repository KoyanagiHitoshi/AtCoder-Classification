N,K=map(int,input().split())
children=[True]*N
for k in range(K):
    d=input()
    A=list(map(int,input().split()))
    for a in A:
        children[a-1]=False
print(children.count(True))