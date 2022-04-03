X=input()
weak="01234567890123"
print("Weak" if X in weak or len(set(list(X)))==1 else "Strong")