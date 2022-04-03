S=input()
T=input()
print(sum(S[i]!=T[i] for i in range(len(S))))