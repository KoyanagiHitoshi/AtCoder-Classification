N=input()
S,T=input().split()
print(*[s+t for s,t in zip(S,T)],sep="")