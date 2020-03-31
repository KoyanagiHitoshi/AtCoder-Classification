import collections
N=int(input())
S=collections.Counter(input() for i in range(N))
maximum=max(S.values())
sort=sorted(key for key,value in S.items() if value==maximum)
for s in sort:
    print(s)