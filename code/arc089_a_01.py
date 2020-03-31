n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
count=0
for i in range(n):
    t,x,y=l[i][0],l[i][1],l[i][2]
    if t>=x+y and t%2==(x+y)%2:
        count+=1
print("Yes" if count==n else "No")