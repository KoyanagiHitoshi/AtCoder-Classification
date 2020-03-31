from collections import Counter
n=int(input())
v=list(map(int,input().split()))
even=Counter(v[0::2]).most_common()
odd=Counter(v[1::2]).most_common()
even.append((0,0))
odd.append((0,0))
if even[0][0]!=odd[0][0]:print(n-(even[0][1]+odd[0][1]))
else:print(min(n-(even[0][1]+odd[1][1]),n-(even[1][1]+odd[0][1])))