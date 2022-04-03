from collections import Counter
N=int(input())
D=Counter(map(int,input().split()))
M=int(input())
T=Counter(map(int,input().split()))
print("NO" if T-D else "YES")