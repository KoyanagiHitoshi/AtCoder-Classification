import math
A,B,W=map(int,input().split())
upper=int(1000*W//A)
lower=int(math.ceil(1000*W/B))
print("UNSATISFIABLE") if lower>upper else print(lower,upper)