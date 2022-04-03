N,M=map(int,input().split())
ac,wa=0,0
task=[0]*N
for m in range(M):
    p,S=input().split()
    p=int(p)-1
    if task[p]!=-1 and S=="WA":
        task[p]+=1
    elif task[p]!=-1 and S=="AC":
        ac+=1
        wa+=task[p]
        task[p]=-1
print(ac,wa)