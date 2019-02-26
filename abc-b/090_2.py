#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
print(len([i for i in map(str,range(a,b+1)) if i==i[::-1]]))
