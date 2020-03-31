N,K=map(int,input().split())
H=[int(input()) for i in range(N)]
H=sorted(H)[::-1]
s=[0]*(N-K+1)
for i in range(N-K+1):
    s[i]=H[i]-H[i+K-1]
print(min(s))