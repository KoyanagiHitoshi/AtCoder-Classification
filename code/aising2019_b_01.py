n=int(input())
a,b=map(int,input().split())
p=list(sorted(map(int,input().split())))
c=d=e=0
for i in range(n):
    if p[i]<=a:c+=1
    elif p[i]<=b:d+=1
    else: e+=1
print(min(c,d,e))