S=input()
print(sum(S[i]!=S[-i-1] for i in range(len(S)//2)))