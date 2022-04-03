N=input()
S,T=input().split()
print("".join(s+t for s,t in zip(S,T)))