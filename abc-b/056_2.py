#!/usr/bin/env python
# -*- conding: utf-8 -*-

w,a,b=map(int,input().split())
print(max(abs(a-b)-w,0))
