import bisect
x = [1, 3, 5, 7, 9]
print(bisect.bisect_right(x, 5))
# 3
"""
x = [1, 3, 5, 7, 9]
     0  1  2  3  4
              ^
"""
