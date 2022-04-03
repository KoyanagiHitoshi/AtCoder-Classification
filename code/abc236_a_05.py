S=input()
a,b=map(int,input().split())
a,b=a-1,b-1
print(S[:a]+S[b]+S[a+1:b]+S[a]+S[b+1:])