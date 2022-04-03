A,B,C=map(int,input().split())
if C%2==0:
    A,B=abs(A),abs(B)
print("<" if A<B else ">" if A>B else "=")