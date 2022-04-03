N=int(input())
for num in range(1,10):
    if (N/num).is_integer() and 1<=(N/num)<=9:
        print("Yes")
        break
else:
    print("No")