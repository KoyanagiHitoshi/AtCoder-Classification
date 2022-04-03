A,B,K=map(int,input().split())
for k in range(K):
    if k%2==0:
        A//=2
        B+=A
    if k%2==1:
        B//=2
        A+=B
print(A,B)