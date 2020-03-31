n=int(input())
w=[input() for i in range(n)]
flag=False
if n==len(set(w)):
    if all([w[i-1][-1]==w[i][0] for i in range(1,n)]):
        flag=True
print("Yes" if flag else "No")