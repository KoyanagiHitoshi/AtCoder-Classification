N=int(input())
weather=[0]*6
for i in range(N):
    MT,mT=map(float,input().split())
    if 35<=MT:
        weather[0]+=1
    if 30<=MT<35:
        weather[1]+=1
    if 25<=MT<30:
        weather[2]+=1
    if 25<=mT:
        weather[3]+=1
    if mT<0 and 0<=MT:
        weather[4]+=1
    if MT<0:
        weather[5]+=1
print(*weather)