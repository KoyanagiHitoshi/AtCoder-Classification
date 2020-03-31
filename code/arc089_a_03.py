N=int(input())
count=0
for i in range(N):
    t,x,y=map(int,input().split())
    if x+y<=t and t%2==(x+y)%2:count+=1
print("Yes" if count==N else "No")