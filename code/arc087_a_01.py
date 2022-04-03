from collections import Counter
N=int(input())
a=Counter(input().split())
count=0
for key,value in a.items():
    key=int(key)
    if key>value:
        count+=value
    elif key<value:
        count+=value-key
print(count)