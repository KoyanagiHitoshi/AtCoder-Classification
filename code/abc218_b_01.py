letters="abcdefghijklmnopqrstuvwxyz"
P=list(map(int,input().split()))
S=[]
for i in range(len(P)):
    S.append(letters[P[i]-1])
print(*S,sep="")