#!/usr/bin/env python
# -*- conding: utf-8 -*-

x = int(input())
c = 0
for i in range(2, 11):    
    c = max(c, int(x**(1/i))**i)
print(c)
