S=input().split("+")
count=0
for s in S:
    if "0" not in s:
        count+=1
print(count)