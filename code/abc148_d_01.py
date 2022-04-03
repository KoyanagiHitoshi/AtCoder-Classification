N=int(input())
A=list(map(int,input().split()))
block=broken=0
for a in A:
    if a-1==block:
        block+=1
    else:
        broken+=1
print(broken if broken!=N else -1)