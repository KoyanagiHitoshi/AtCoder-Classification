A,B=input().split()
print("Hard" if any(int(a)+int(b)>=10 for a,b in zip(A[::-1],B[::-1])) else "Easy")