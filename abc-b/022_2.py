#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=[int(input()) for _ in range(n)]
print(len(l)-len(set(l)))
