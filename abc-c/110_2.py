#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=sorted(map(list(input()).count,set(s)))
t=sorted(map(list(input()).count,set(t)))
print("Yes" if s==t else "No")
