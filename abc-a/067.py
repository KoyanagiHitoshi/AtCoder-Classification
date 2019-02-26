#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
print("Impossible" if a*b*(a+b)%3 else "Possible")
