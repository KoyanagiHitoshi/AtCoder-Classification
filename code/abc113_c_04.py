import collections,bisect
N,M=map(int,input().split())
PY=[list(map(int,input().split())) for i in range(M)]
x=collections.defaultdict(list)
for city,year in sorted(PY):
    x[city]+=[year]
for city,year in PY:
    num=bisect.bisect(x[city],year)
    print("%06d%06d"%(city,num))