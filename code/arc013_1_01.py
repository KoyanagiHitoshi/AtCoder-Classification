from itertools import permutations
N,M,L=map(int,input().split())
PQR=list(map(int,input().split()))
count=0
for P,Q,R in permutations(PQR):
    count=max(count,(N//P)*(M//Q)*(L//R))
print(count)