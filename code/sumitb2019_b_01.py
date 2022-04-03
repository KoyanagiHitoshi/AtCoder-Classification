import math
N=int(input())
price=math.ceil(N/1.08)
print(price if math.floor(price*1.08)==N else ":(")