import collections,bisect
N,M=map(int,input().split())
PY=[list(map(int,input().split())) for i in range(M)]
a=collections.defaultdict(list)
for city,year in sorted(PY):a[city]+=[year]
for city,year in PY:
    z=bisect.bisect(a[city],year)
    print("%06d%06d"%(city,z))