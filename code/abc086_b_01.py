a,b=map(str,input().split())
c=int(a+b)
print("Yes" if c==(int(c**(1/2))**2) else "No")