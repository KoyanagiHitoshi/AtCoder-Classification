N=int(input())
S=list(input())
Q=int(input())
t=0
for q in range(Q):
    T,A,B=map(int,input().split())
    if T==1:
        A,B=A-1,B-1
        if t:
            A=(A+N)%(2*N)
            B=(B+N)%(2*N)
        S[A],S[B]=S[B],S[A]
    else:
        t^=1
if t:
    S=S[N:]+S[:N]
print("".join(S))