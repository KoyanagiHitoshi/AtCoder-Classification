#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
m=n
for i in range(1,n+1):
  a=n-(i*(n//i))+abs(i-(n//i))
  if m>a:
    m=a
print(m)
