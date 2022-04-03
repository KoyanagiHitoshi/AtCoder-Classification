N=int(input())
S=input()
print(max(len(set(S[:i])&set(S[i:])) for i in range(N)))