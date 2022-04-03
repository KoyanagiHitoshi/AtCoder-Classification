a,b,c=map(int,input().split())
print("Yes" if c-a-b>0 and 4*a*b<(c-a-b)**2 else "No")