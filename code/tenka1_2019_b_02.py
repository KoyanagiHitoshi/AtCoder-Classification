input()
S=input()
k=int(input())
i=S[k-1]
for s in S:print(s if s==i else "*",end="")