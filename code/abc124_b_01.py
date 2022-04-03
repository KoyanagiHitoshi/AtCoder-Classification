N=int(input())
H=list(map(int,input().split()))
count=0
base=0
for h in H:
    if base<=h:
        count+=1
        base=h
print(count)