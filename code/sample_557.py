import bisect
x = [1, 1, 1, 3, 3, 3, 5, 5, 5]
bisect.insort_left(x, 3)
print(x)
# [1, 1, 1, 3, 3, 3, 3, 5, 5, 5]
"""
x = [1, 1, 1, 3, 3, 3, 3, 5, 5, 5]
     0  1  2  3  4  5  6  7  8  9
              ^
"""
