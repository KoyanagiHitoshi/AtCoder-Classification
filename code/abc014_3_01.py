n=int(input())
color=10**6+1
check=[0]*(color+1)
for i in range(n):
    a,b=map(int,input().split())
    check[a]+=1
    check[b+1]-=1
for i in range(color):
    check[i+1]+=check[i]
print(max(check))