#!/usr/bin/env python
# -*- conding: utf-8 -*-

l=[int(_) for _ in input().split()]
print(max(l)*2**int(input())+sum(l)-max(l))
