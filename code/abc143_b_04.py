import itertools
N=int(input())
D=list(map(int,input().split()))
print((sum(D)**2-sum(d*d for d in D))//2)