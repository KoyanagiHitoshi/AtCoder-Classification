N,W=map(int,input().split())
AB=[]
for i in range(N):
    A,B=map(int,input().split())
    AB.append([A,B])
AB.sort(reverse=True)
total=0
for i in range(N):
    total+=AB[i][0]*min(AB[i][1],W)
    W-=AB[i][1]
    if W<=0:
        break
print(total)