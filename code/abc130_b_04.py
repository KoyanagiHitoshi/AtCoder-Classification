N,X=map(int,input().split())
L=list(map(int,input().split()))
cumulative,count=0,1
for l in L:
    cumulative+=l
    if cumulative<=X:count+=1
print(count)