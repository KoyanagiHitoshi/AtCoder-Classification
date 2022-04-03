X=input()
weak="01234567890123"
print("Weak" if X in weak or int(X)%1111==0 else "Strong")