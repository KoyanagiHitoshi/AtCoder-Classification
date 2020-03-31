N,K=map(int,input().split())
TD=[[int(j) for j in input().split()] for i in range(N)]
TD=sorted(TD,key=lambda x:-x[1])
point=0
stack=[]
kind=set()
for t,d in TD[:K]:
    point+=d
    if t in kind:stack.append(d)
    else:kind.add(t)
point=point+len(kind)**2
ans=point
for t,d in TD[K:]:
    if not stack:break
    if not t in kind:
        point+=d-stack.pop()+2*len(kind)+1
        kind.add(t)
        ans=max(ans,point)
print(ans)