#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
c,d=map(int,input().split())
print("YES" if a==c or a==d or b==c or b==d else "NO")
