N=int(input())
A=list(map(int,input().split()))
count=[0]*401
for a in A:
    count[a+200]+=1
ans=0
for i in range(401):
    for j in range(401):
        ans+=count[i]*count[j]*((i-200)-(j-200))**2
print(ans//2)