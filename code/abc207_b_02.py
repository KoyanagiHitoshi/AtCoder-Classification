import math
A, B, C, D = map(int, input().split())
count = -1
diff = C*D-B
if diff > 0:
    count = math.ceil(A/diff)
print(count)