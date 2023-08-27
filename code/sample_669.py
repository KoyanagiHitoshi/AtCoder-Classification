import numpy
x = numpy.array([[".", ".", "#"], ["#", ".", "."], [".", "#", "."]])
print(numpy.argwhere(x == "#"))
