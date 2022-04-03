N=int(input())
S=input()
count=S.count("E")
minimum=count
for s in S:
    if s=="E":
        count-=1
    else:
        count+=1
    minimum=min(minimum,count)
print(minimum)