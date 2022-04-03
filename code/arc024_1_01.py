from collections import Counter
L,R=map(int,input().split())
l=Counter(input().split())
r=Counter(input().split())
print(sum([min(value,l[key]) for key,value in r.items()]))