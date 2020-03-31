N=int(input())
F=[int(input().replace(' ',''),2) for i in range(N)]
P=[list(map(int,input().split())) for i in range(N)]
print(max(sum([p[bin(f&i).count('1')] for f,p in zip(F,P)]) for i in range(1,2**10)))