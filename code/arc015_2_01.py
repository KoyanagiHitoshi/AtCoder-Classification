N=int(input())
weather=[0]*6
for i in range(N):
    MT,mT=map(float,input().split())
    weather[0]+=35<=MT
    weather[1]+=30<=MT<35
    weather[2]+=25<=MT<30
    weather[3]+=25<=mT
    weather[4]+=mT<0 and 0<=MT
    weather[5]+=MT<0
print(*weather)