import bisect
x = [1, 3, 5, 7, 9]
bisect.insort_right(x, 5)
print(x)
# [1, 3, 5, 5, 7, 9]
"""
x = [1, 3, 5, 5, 7, 9]
     0  1  2  3  4  5
              ^
"""
