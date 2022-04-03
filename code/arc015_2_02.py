N=int(input())
weather=[0]*6
for i in range(N):
    MT,mT=map(float,input().split())
    if MT>=35:
        weather[0]+=1
    elif MT>=30:
        weather[1]+=1
    elif MT>=25:
        weather[2]+=1
    if mT>=25:
        weather[3]+=1
    if MT>=0 and mT<0:
        weather[4]+=1
    elif MT<0:
        weather[5]+=1
print(*weather)