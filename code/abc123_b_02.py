from itertools import permutations
import math
menu=5
ABCDE=[int(input()) for i in range(menu)]
orders=list(permutations(ABCDE,menu))
minimum=sum(math.ceil(time/10)*10 for time in ABCDE)
for order in orders:
    total=order[0]
    for i in range(1,menu):
        total+=math.ceil(order[i]/10)*10
    minimum=min(minimum,total)
print(minimum)