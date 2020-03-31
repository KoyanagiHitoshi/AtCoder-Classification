import itertools
N=int(input())
S=[]
count=0
for i in range(10):
    S+=itertools.product("753",repeat=i)
for s in S:
    if len(set(s))>2 and int("".join(s))<=N:count+=1
print(count)