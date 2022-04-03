A,B,C=map(int,input().split())
if C%2==0:
    print("<" if abs(A)<abs(B) else ">" if abs(A)>abs(B) else "=")
else:
    print("<" if A<B else ">" if A>B else "=")