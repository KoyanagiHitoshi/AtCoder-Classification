from collections import Counter
n=int(input())
v=list(map(int,input().split()))
odd=Counter(v[0::2]).most_common()
even=Counter(v[1::2]).most_common()
odd.append([0,0])
even.append([0,0])
if odd[0][0]!=even[0][0]:
    print(n-(odd[0][1]+even[0][1]))
else:
    print(min(n-(odd[1][1]+even[0][1]),n-(odd[0][1]+even[1][1])))