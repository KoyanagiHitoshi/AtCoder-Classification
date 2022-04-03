N=int(input())
S=[]
T=[]
for i in range(N):
    s,t=input().split()
    S.append(s)
    T.append(int(t))
print(S[T.index(sorted(T)[-2])])