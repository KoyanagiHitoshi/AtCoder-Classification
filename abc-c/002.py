#!/usr/bin/env python
# -*- conding: utf-8 -*-

x1,y1,x2,y2,x3,y3=map(int,input().split())
a=((x1-x2)**2+(y1-y2)**2)**.5
b=((x2-x3)**2+(y2-y3)**2)**.5
c=((x3-x1)**2+(y3-y1)**2)**.5
s=(a+b+c)/2
print((s*(s-a)*(s-b)*(s-c))**.5)
