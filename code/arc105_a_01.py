A,B,C,D=sorted(map(int,input().split()))
print("Yes" if A+D==B+C or A+B+C==D else "No")