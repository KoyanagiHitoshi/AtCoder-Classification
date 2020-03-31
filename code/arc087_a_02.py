from collections import Counter
n=int(input())
a=Counter(input().split())
ans=0
for i,j in a.items():
    i=int(i)
    if i>j:
        ans+=j
    elif i<j:
        ans+=j-i
print(ans)