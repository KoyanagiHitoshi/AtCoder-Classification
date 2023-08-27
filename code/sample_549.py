import bisect
x = [1, 1, 1, 3, 3, 3, 5, 5, 5]
print(bisect.bisect_left(x, 3))
# 3
"""
x = [1, 1, 1, 3, 3, 3, 5, 5, 5]
     0  1  2  3  4  5  6  7  8
              ^
"""
