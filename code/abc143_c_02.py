N=int(input())
S=input()
print(sum(S[n]!=S[n-1] for n in range(1,N))+1)