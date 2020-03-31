from collections import Counter
n=int(input())
v=list(map(int,input().split()))
a=Counter(v[0::2]).most_common()
b=Counter(v[1::2]).most_common()
a.append([0,0])
b.append([0,0])
if a[0][0]!=b[0][0]:
    print(n-(a[0][1]+b[0][1]))
else:
    print(min(n-(a[1][1]+b[0][1]),n-(a[0][1]+b[1][1])))