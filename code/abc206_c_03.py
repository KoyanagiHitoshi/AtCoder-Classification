import collections
N=int(input())
A=collections.Counter(list(map(int,input().split())))
ans=0
for value in A.values():
    ans+=(N-value)*value
print(ans//2)