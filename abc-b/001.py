#!/usr/bin/env python
# -*- conding: utf-8 -*-

a=int(input())
b=a/1000
if b < 0.1:c=0
elif 0.1<=b<=5:
    c=b*10
    print
elif 6<=b<=30:
    c=b+50
elif 35<=b<=70:
    c=(b-30)/5+80
else:
    c=89
print("{0:02d}".format(int(c)))
