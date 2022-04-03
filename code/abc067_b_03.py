N,K=map(int,input().split())
L=list(map(int,input().split()))
stick=[0]*K
for l in L:
    minimum=min(stick)
    if l>minimum:
        stick.remove(minimum)
        stick.append(l)
print(sum(stick))