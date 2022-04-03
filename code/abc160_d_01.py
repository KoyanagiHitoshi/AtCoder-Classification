N,X,Y=map(int,input().split())
count=[0]*N
for i in range(1,N):
    for j in range(i+1,N+1):
        distance=min(j-i,abs(j-X)+abs(i-Y)+1,abs(j-Y)+abs(i-X)+1)
        count[distance]+=1
print(*count[1:],sep="\n")