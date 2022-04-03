N,X,Y=map(int,input().split())
distance=[0]*N
for i in range(1,N):
    for j in range(i+1,N+1):
        k=min(j-i,abs(j-X)+abs(i-Y)+1,abs(j-Y)+abs(i-X)+1)
        distance[k]+=1
print(*distance[1:],sep="\n")