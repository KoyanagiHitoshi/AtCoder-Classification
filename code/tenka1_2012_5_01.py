a,b,c=map(int,input().split())
for num in range(1,128):
    if num%3==a and num%5==b and num%7==c:
        print(num)