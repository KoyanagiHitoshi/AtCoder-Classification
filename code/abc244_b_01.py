N=int(input())
T=input()
R=0
count=[0]*4
for i in range(N):
    if T[i]=="S":
        count[R%4]+=1
    else:
        R+=1
print(count[0]-count[2],count[3]-count[1])