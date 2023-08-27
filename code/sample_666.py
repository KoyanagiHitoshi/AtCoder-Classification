import numpy
x = numpy.array([[3, 1, 2], [2, 3, 1]])
ind = numpy.argsort(x, axis=0)
print(ind)
print(numpy.take_along_axis(x, ind, axis=0))
