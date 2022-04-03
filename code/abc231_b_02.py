N=int(input())
S=[input() for i in range(N)]
print(max(S,key=S.count))