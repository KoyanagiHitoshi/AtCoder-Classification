N=input()
S=input()
count,max_count=0,0
for s in S:
    if s=="I":
        count+=1
    else:
        count-=1
    max_count=max(max_count,count)
print(max_count)