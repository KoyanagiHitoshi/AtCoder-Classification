A,B=map(int,input().split())
print(1 if A+B>=15 and B>=8 else 2 if A+B>=10 and B>=3 else 3 if A+B>=3 else 4)