S=input()
T=input()
print(sum(s!=t for s,t in zip(S,T)))