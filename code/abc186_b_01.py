H,W=map(int,input().split())
A=[]
for i in range(H):
    a=list(map(int,input().split()))
    for j in range(W):
        A.append(a[j])
print(sum(a-min(A) for a in A))