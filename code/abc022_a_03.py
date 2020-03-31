n,s,t=map(int,input().split())
w=c=0
for i in range(n):
    w+=int(input())
    if(s<=w<=t):c+=1
print(c)