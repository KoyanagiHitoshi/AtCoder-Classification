A,B=map(int,input().split())
print("Draw" if A==B else "Bob" if (A+13)%15<(B+13)%15 else "Alice")