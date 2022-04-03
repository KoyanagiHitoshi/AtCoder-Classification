N=int(input())
t=set()
T=set()
for i in range(N):
    S=input()
    if S[0]=="!":
        t.add(S[1:])
    else:
        T.add(S)
print("satisfiable" if len(T&t)==0 else (T&t).pop())