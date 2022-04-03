import itertools
import collections
N=int(input())
A=list(itertools.accumulate(map(int,input().split())))
count=0
for s in collections.Counter(A+[0]).values():
    count+=s*(s-1)//2
print(count)