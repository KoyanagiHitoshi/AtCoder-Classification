N=int(input())
for i in range(1,10):
    m=N/i
    if m.is_integer() and 1<=m<=9:
        print("Yes")
        break
else:
    print("No")