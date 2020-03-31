N,X=map(int,input().split())
L=list(map(int,input().split()))
cum,count=0,1
for l in L:
    cum+=l
    if cum<=X:count+=1
print(count)