import collections
N=int(input())
s=[str(sorted(input())) for i in range(N)]
counter_s=collections.Counter(s)
print(sum((v*(v-1))//2 for v in counter_s.values()))