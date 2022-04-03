import math
P = int(input())
count = 0
for coin in range(10, 0, -1):
    if P >= math.factorial(coin):
        count += P//math.factorial(coin)
        P %= math.factorial(coin)
print(count)