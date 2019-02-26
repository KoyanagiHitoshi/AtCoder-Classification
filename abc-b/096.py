#!/usr/bin/env python
# -*- conding: utf-8 -*-

l=[int(_) for _ in input().split()]
k=int(input())
print(max(l)*2**k+sum(l)-max(l))
