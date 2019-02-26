#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,n=(int(input()) for _ in range(3))
while n%a!=0 or n%b!=0:n+=1
print(n)
