A,B,K,L=map(int,input().split())
if A<B/L:
    print(A*K)
else:
    mod=K%L
    div=K//L
    if A*mod<B:
        print(div*B+mod*A)
    else:
        print(div*B+B)