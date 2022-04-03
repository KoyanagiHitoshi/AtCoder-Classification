A,B,C=map(int,input().split())
print("?" if A+B==C and A-B==C else "+" if A+B==C else "-" if A-B==C else "!")