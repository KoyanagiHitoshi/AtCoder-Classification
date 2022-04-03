A,B,C,X=[int(input()) for i in range(4)]
print([500*a+100*b+50*c for c in range(C+1) for b in range(B+1) for a in range(A+1)].count(X))