#!/usr/bin/env python
# -*- conding: utf-8 -*-

t=""
for x in input():
    if x=="B":t=t[:-1];print(t)
    else:t+=x
print(t)
