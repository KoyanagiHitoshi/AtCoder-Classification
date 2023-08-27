import bisect
x = [1, 3, 5, 7, 9]
bisect.insort_left(x, 6)
print(x)
# [1, 3, 5, 6, 7, 9]
"""
x = [1, 3, 5, 6, 7, 9]
     0  1  2  3  4  5
              ^
"""
