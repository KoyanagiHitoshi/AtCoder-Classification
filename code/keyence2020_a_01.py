import math
H,W,N=[int(input()) for i in range(3)]
print(math.ceil(N/max(H,W)))