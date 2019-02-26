#!/usr/bin/env python
# -*- conding: utf-8 -*-

h,w=map(int,input().split())
pattern=[h//2+w//3+1,h//3+w//2+1,h,w]
if h%3==0 or w%3==0:
    pattern+=[0]
if h%2==0:
    pattern+=[h//2]
if w%2==0:
    pattern+=[w//2]
print(min(pattern))
