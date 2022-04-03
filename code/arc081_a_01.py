from collections import Counter
N=int(input())
A=Counter(list(map(int,input().split())))
length=[0,0]
for a in A:
    if A[a]>=2:
        length.append(a)
    if A[a]>=4:
        length.append(a)
length.sort()
print(length[-1]*length[-2])