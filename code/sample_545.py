import bisect
x = [1, 3, 5, 7, 9]
print(bisect.bisect_left(x, 5))
# 2
"""
x = [1, 3, 5, 7, 9]
     0  1  2  3  4
           ^
"""
