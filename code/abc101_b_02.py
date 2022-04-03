N=input()
print("Yes" if int(N)%sum(int(n) for n in N)==0 else "No")