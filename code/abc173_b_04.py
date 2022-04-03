from collections import Counter
N=int(input())
S=Counter(input() for i in range(N))
judge=["AC","WA","TLE","RE"]
for status in judge:
    print("{0} x {1}".format(status,S[status]))