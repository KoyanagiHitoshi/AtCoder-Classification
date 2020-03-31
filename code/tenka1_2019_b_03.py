input()
S=input()
k=int(input())
for s in S:print(s if s==S[k-1] else "*",end="")