A=int(input())
for i in range(A+1):
    if i**3==A:
        print("YES")
        break
else:
    print("NO")