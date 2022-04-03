N,K=map(int,input().split())
children=[0]*N
for k in range(K):
    d=input()
    A=list(map(int,input().split()))
    for a in A:
        children[a-1]+=1
print(children.count(0))