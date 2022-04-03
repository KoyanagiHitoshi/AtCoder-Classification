N,K=map(int,input().split())
children=[False]*N
for i in range(K):
    input()
    A=list(map(int,input().split()))
    for a in A:
        children[a-1]=True
print(children.count(False))