H,W=map(int,input().split())
pattern=[H//2+W//3+1,H//3+W//2+1,H,W]
if H%3==0 or W%3==0:
    pattern+=[0]
if H%2==0:
    pattern+=[H//2]
if W%2==0:
    pattern+=[W//2]
print(min(pattern))