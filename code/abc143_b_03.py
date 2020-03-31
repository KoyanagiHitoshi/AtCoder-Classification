import itertools
N=int(input())
D=list(map(int,input().split()))
print(sum(d*cumulate for d,cumulate in zip(D[1:],itertools.accumulate(D))))