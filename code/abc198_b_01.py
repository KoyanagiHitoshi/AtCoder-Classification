N=input()
for i in range(len(N)):
    if N[-1]!="0":
        break
    else:
        N=N[:-1]
print("Yes" if N==N[::-1] else "No")