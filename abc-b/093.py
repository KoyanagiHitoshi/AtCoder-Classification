#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,k = map(int, input().split())
r = range(a,b+1)
for i in sorted(set(r[:3])|set(r[-3:])):
    print(i)
