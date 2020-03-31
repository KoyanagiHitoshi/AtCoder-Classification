N,L=map(int,input().split())
S=list(input())
tab=1
clash=0
for s in S:
    if s=="+":tab+=1
    else:tab-=1
    if tab>L:
        clash+=1
        tab=1
print(clash)