N=int(input())
S=[]
P=[]
for i in range(N):
    s,p=input().split()
    S.append(s)
    P.append(int(p))
print(S[P.index(max(P))] if max(P)>sum(P)/2 else "atcoder")