S=input()
print(sum(1 for i in range(len(S)//2) if S[i]!=S[-i-1]))