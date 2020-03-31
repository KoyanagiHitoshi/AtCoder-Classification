n,s,t=map(int,input().split())
w=c=0
for i in range(n):
    w+=int(input())
    c+=s<=w<=t
print(c)