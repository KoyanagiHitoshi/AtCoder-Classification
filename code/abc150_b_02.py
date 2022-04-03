N=int(input())
S=input()
print(sum(S[i:i+3]=="ABC" for i in range(N-2)))