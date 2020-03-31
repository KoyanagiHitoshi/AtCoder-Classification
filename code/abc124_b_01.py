n=int(input())
H=list(map(int,input().split()))
p=0
count=0
for h in H:
    if p<=h:
        p=max(p,h)
        count+=1
print(count)