from collections import Counter
N=int(input())
D=Counter(map(int,input().split()))
M=int(input())
T=Counter(map(int,input().split()))
print("YES" if all(D[key]>=value for key,value in T.items()) else "NO")