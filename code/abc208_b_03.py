import math
P=int(input())
count=0
for coin in range(10,0,-1):
    while P>=math.factorial(coin):
        count+=1
        P-=math.factorial(coin)
print(count)