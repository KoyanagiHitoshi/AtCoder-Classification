#!/usr/bin/env python
# -*- conding: utf-8 -*-

w,a,b=map(int,input().split())
print(max(b-a-w,0) if a<b else max(a-b-w,0))
