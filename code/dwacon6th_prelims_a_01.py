N=int(input())
S,T=[],[]
for i in range(N):
    s,t=input().split()
    S.append(s)
    T.append(int(t))
X=input()
print(sum(T[S.index(X)+1:]))