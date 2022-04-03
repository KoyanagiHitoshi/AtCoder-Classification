N,M=map(int,input().split())
A=input().split()
B=input().split()
flag=True
for b in B:
    if b not in A:
        flag=False
        break
    else:
        A.remove(b)
print("Yes" if flag else "No")