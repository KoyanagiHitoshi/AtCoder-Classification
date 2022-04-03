import collections
N,M=map(int,input().split())
A=list(map(int,input().split()))
key,value=collections.Counter(A).most_common()[0]
print(key if value>N/2 else "?")