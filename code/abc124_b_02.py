n=int(input())
b=c=0
for h in map(int,input().split()):
    if b<=h:
        b=h
        c+=1
print(c)