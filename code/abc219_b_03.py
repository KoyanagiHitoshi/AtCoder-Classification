S=[input() for i in range(3)]
T=input()
print("".join(S[int(t)-1] for t in T))