from collections import Counter
N=int(input())
S=[input() for i in range(N)]
s=Counter(S)
judge=["AC","WA","TLE","RE"]
for j in judge:
    print("{0} x {1}".format(j,s[j]))