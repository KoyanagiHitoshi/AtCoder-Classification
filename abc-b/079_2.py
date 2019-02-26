#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=2,1
for i in range(int(input())):
    a,b=b,a+b
print(a)
