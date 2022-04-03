import itertools
N,M,Q=map(int,input().split())
q=[list(map(int,input().split())) for i in range(Q)]
point=0
for A in itertools.combinations_with_replacement(range(1,M+1),N):
    point=max(point,sum(d for a,b,c,d in q if A[b-1]-A[a-1]==c))
print(point)