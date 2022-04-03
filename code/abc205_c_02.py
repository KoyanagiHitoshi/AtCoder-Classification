A,B,C=map(int,input().split())
if C%2==0:
    C=2
else:
    C=1
print("<" if A**C<B**C else ">" if A**C>B**C else "=")