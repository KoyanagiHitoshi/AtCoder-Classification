A,B,C=map(int,input().split())
C=C%2+2
print("<" if A**C<B**C else ">" if A**C>B**C else "=")