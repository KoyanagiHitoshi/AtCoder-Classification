N=int(input())
S=input()
print(sum(S[i]!=S[i-1] for i in range(1,N))+1)