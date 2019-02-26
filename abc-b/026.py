#!/usr/bin/env python
# -*- conding: utf-8 -*-

r=sorted(int(input())**2 for i in range(int(input())))[::-1]
print((sum(r[::2])-sum(r[1::2]))*355/113)
