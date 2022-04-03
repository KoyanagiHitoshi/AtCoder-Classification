def prize(n):
    if n==0 or n==1:
        return 100
    elif n==2:
        return 200
    else:
        return prize(n-1)+prize(n-2)+prize(n-3)
print(prize(19))