N,M=map(int,input().split())
A=input().split()
B=input().split()
flag=True
for b in B:
    if b in A:
        A.remove(b)
    else:
        flag=False
        break
print("Yes" if flag else "No")