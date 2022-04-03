A,B=map(int,input().split())
print("Possible" if A*B*(A+B)%3==0 else "Impossible")