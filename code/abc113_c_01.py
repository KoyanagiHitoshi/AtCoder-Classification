import collections
import bisect
N,M=map(int,input().split())
PY=[[int(j) for j in input().split()] for i in range(M)]
dict_PY=collections.defaultdict(list)
for p,y in sorted(PY):
    dict_PY[p]+=[y]
for p,y in PY:
    number=bisect.bisect(dict_PY[p],y)
    print("%06d%06d"%(p,number))