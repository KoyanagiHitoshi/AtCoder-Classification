from collections import Counter
N=int(input())
D=Counter(map(int,input().split()))
M=int(input())
T=Counter(map(int,input().split()))
D.subtract(T)
print("NO" if -D else "YES")