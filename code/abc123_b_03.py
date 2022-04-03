import math
orders=[int(input()) for i in range(5)]
maximum,total=0,0
for order in orders:
    time=math.ceil(order/10)*10
    total+=time
    remaine=time-order
    maximum=max(maximum,remaine)
print(total-maximum)