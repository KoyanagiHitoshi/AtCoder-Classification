N=int(input())
P=list(map(int,input().split()))
count,minimum=0,max(P)
for i in range(N):
    if P[i]<=minimum:
        count+=1
        minimum=P[i]
print(count)