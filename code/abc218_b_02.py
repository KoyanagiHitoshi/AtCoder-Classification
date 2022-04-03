P=list(map(int,input().split()))
S=[]
for i in range(len(P)):
    S.append(chr(96+P[i]))
print(*S,sep="")