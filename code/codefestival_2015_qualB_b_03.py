from collections import Counter
N,M=map(int,input().split())
A=list(map(int,input().split()))
key,value=Counter(A).most_common()[0]
print(key if value>N/2 else "?")