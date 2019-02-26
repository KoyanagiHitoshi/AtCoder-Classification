#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,n=(int(input()) for _ in [0]*3)
while n%a+n%b:n+=1
print(n)
