import itertools
N=int(input())
count=0
S=[]
for i in range(10):
    S+=list(itertools.product("357",repeat=i))
for s in S:
    if len(set(s))>2 and int("".join(s))<=N:
        count+=1
print(count)